# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.db.models import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#from django.views.decorators.cache import cache_page

#from . import settings
from . models import CatalogPost, CatalogCategory, CatalogPostImages
from . forms import CatalogEditForm, ImageUploadForm
from common.utils import log
from location.models import Country, City


def get_categories():
    return CatalogCategory.objects.get_query_set()

def get_countries( category = None ):
#    log( category )
    if category:
        cots = CatalogPost.objects.filter( category = category ).values_list( 'country' ).distinct()
    else:
        cots = CatalogPost.objects.values_list( 'country' ).distinct()
#    log( cots )
    countries = Country.objects.filter( pk__in = cots )
#    log( countries )
    return countries

def get_posts( category = None, country = None, city = None, page = None ):
    posts = CatalogPost.objects.filter( status = 'active' )

    if category:
        posts = posts.filter( category = category )

    if country:
        posts = posts.filter( country = country )

    if city:
        posts = posts.filter( city = city )

    paginator = Paginator( posts, 7 )

    try:
        posts = paginator.page( page )
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page( 1 )
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page( paginator.num_pages )

    return posts

def home( request, country = None, city = None, page = None ):

    countries = get_countries()
    categories = get_categories()
    posts = get_posts( country = country, city = city, page = page )

    data = {
        'countries' : countries,
        'categories' : categories,
        'posts' : posts,
    }
    return render( request, 'catalog/home.html', data )


def category( request, id, slug = None, country = None, city = None, page = None ):

    id = int( id )

    try:
        category = CatalogCategory.objects.get( pk = id )
    except CatalogCategory.DoesNotExist:
        raise Http404

    if category.slug() != slug:
        return redirect( 'catalog-category', id = id, slug = category.slug(), permanent = True )

    countries = get_countries( category )
    categories = get_categories()
    posts = get_posts( category = category, country = country, city = city, page = page )

    data = {
        'category':category,
        'posts':posts,
        'categories':categories,
        'countries' : countries,
    }

    return render( request, 'catalog/category.html', data )

def post( request, id, slug = None ):
    id = int( id )

    try:
        post = CatalogPost.objects.get( pk = id )
    except CatalogPost.DoesNotExist:
        raise Http404

    if post.slug() != slug:
        return redirect( 'catalog-post', id = id, slug = post.slug(), permanent = True )

    data = {
        'post':post,
        'categories':CatalogCategory.objects.all(),
    }

    return render( request, 'catalog/post.html', data )

@login_required
def add( request ):
    if request.session.get( 'catalog-draft-id', '' ) and int( request.session['catalog-draft-id'] ) > 0:
        return redirect( 'catalog-edit', id = request.session['catalog-draft-id'] )
    else:
        post = CatalogPost( 
            status = 'draft',
            author = User.objects.get( pk = request.user.id )
        )
        post.save()
        request.session['catalog-draft-id'] = post.id
        return redirect( 'catalog-edit', id = post.id )


@login_required
def edit( request, id ):
    id = int( id )

    try:
        post = CatalogPost.objects.get( pk = id )
    except CatalogPost.DoesNotExist:
        raise Http404

    user = User.objects.get( pk = request.user.id )

    if post.author.id != user.id:
        return redirect( '/accounts/login/' )

    form = CatalogEditForm( instance = post )

    if request.method == "POST":
        form = CatalogEditForm( request.POST, instance = post )
        if form.is_valid():
            form.save()
            post.status = 'active'
            post.save()

            try:
                del request.session['catalog-draft-id']
            except :
                pass

            return redirect( 'catalog-post', id = id )

    images = CatalogPostImages.objects.filter( post = post )

    data = {
        'post':post,
        'form':form,
        'image_upload_form':ImageUploadForm( initial = {'post':post} ),
        'images':images,
    }
    return render( request, 'catalog/edit.html', data )

def file( request ):

    post = CatalogPostImages.objects.get( pk = 1 )

    if request.method == "POST":
        form = ImageUploadForm( request.POST, request.FILES )
        if form.is_valid():
            form.save()
    else:
        form = ImageUploadForm( initial = {'post':post} )


    images = CatalogPostImages.objects.filter( post = 1 )

    data = {
        'form':form,
        'images':images,
    }
    return render( request, 'catalog/file.html', data )
