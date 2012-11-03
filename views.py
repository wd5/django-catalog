# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect

from zokiguide.decorators import render_to

#from . import settings
from . models import Post, Category
from . forms import CatalogEditForm



@render_to( 'catalog/home.html' )
def home( request ):
    data = {}
    return data

@login_required
def add( request ):
    if request.session.get( 'catalog-draft-id', '' ) and int( request.session['catalog-draft-id'] ) > 0:
        return redirect( 'catalog-edit', id = request.session['catalog-draft-id'] )
    else:
        post = Post( status = 'draft', author = User.objects.get( pk = request.user.id ) )
        post.save()
        request.session['catalog-draft-id'] = post.id
        return redirect( 'catalog-edit', id = post.id )

@render_to( 'catalog/category.html' )
def category( request, id, slug = None ):

    id = int( id )

    try:
        category = Category.objects.get( pk = id )
    except Category.DoesNotExist:
        raise Http404

    if category.slug() != slug:
        return redirect( 'catalog-category', id = id, slug = category.slug(), permanent = True )

    data = {
        'category':category,
        'posts':Post.objects.filter( category = id )[:10],
        'categories':Category.objects.all(),
    }

    return data

@render_to( 'catalog/post.html' )
def post( request, id, slug = None ):
    id = int( id )

    try:
        post = Post.objects.get( pk = id )
    except Post.DoesNotExist:
        raise Http404

    if post.slug() != slug:
        return redirect( 'catalog-post', id = id, slug = post.slug(), permanent = True )

    data = {
        'post':post,
        'categories':Category.objects.all(),
    }

    return data

@login_required
@render_to( 'catalog/edit.html' )
def edit( request, id ):
    id = int( id )

    try:
        post = Post.objects.get( pk = id )
    except Post.DoesNotExist:
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

    data = {
        'form':form
    }
    return data
