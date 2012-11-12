# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect


from django.views.decorators.cache import cache_page

from zokiguide.decorators import render_to

#from . import settings
from . models import CatalogPost, CatalogCategory, CatalogPostImages
from . forms import CatalogEditForm, ImageUploadForm
from common.utils import log
from location.models import Country, City



def get_categories():
    return CatalogCategory.objects.all()

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

def get_posts( category = None, country = None, city = None ):
    posts = CatalogPost.objects.filter( status = 'active' )

    if category:
        posts = posts.filter( category = category )

    if country:
        posts = posts.filter( country = country )

    if city:
        posts = posts.filter( city = city )

    posts = posts[:10]

    return posts

@cache_page( 60 * 15 )
@render_to( 'catalog/home.html' )
def home( request ):
    countries = get_countries()
    categories = get_categories()
    posts = get_posts()

    data = {
        'countries':countries,
        'categories':categories,
        'posts':posts,
    }
    return data

@render_to( 'catalog/category.html' )
def category( request, id, slug = None ):

    id = int( id )

    try:
        category = CatalogCategory.objects.get( pk = id )
    except CatalogCategory.DoesNotExist:
        raise Http404

    if category.slug() != slug:
        return redirect( 'catalog-category', id = id, slug = category.slug(), permanent = True )

    countries = get_countries( category )
    categories = get_categories()
    posts = get_posts( category = category )

    data = {
        'category':category,
        'posts':posts,
        'categories':categories,
    }

    return data

@login_required
def add( request ):
    if request.session.get( 'catalog-draft-id', '' ) and int( request.session['catalog-draft-id'] ) > 0:
        return redirect( 'catalog-edit', id = request.session['catalog-draft-id'] )
    else:
        post = CatalogPost( status = 'draft', author = User.objects.get( pk = request.user.id ) )
        post.save()
        request.session['catalog-draft-id'] = post.id
        return redirect( 'catalog-edit', id = post.id )



@render_to( 'catalog/post.html' )
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

    return data

@login_required
@render_to( 'catalog/edit.html' )
def edit( request, id ):
    id = int( id )

    import logging
    # Get an instance of a logger
    logger = logging.getLogger( 'zoki' )
    logger.debug( id )

    try:
        post = CatalogPost.objects.get( pk = id )
    except CatalogPost.DoesNotExist:
        raise Http404

    if request.method == "POST":
        form = CatalogEditForm( request.POST, instance = post )
        if form.is_valid:
            form.save()
            post.status = 'active'
            post.save()

            return redirect( 'catalog-post', id = id )
    else:
        form = CatalogEditForm( instance = post )

    images = CatalogPostImages.objects.filter( post = post )

    data = {
        'post':post,
        'form':form,
        'image_upload_form':ImageUploadForm( initial = {'post':post} ),
        'images':images,
    }
    return data

@render_to( 'catalog/file.html' )
def file( request ):
#    form = ImageUploadForm()
    post = CatalogPostImages.objects.get( pk = 1 )

    if request.method == "POST":
        form = ImageUploadForm( request.POST, request.FILES )
        if form.is_valid:
            form.save()
    else:
        form = ImageUploadForm( initial = {'post':post} )


    images = CatalogPostImages.objects.filter( post = 1 )

    data = {
        'form':form,
        'images':images,
    }
    return data

