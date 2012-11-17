from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
#from django.forms.models import inlineformset_factory

from common.forms import CommonPostEditForm
from . models import CatalogPost, CatalogCategory, CatalogPostImages

class CatalogEditForm( CommonPostEditForm ):
    category = forms.ModelMultipleChoiceField( 
        queryset = CatalogCategory.objects.all(),
        required = False,
        widget = FilteredSelectMultiple( 
            'categories',
            False,
        )
    )

    class Meta( CommonPostEditForm.Meta ):
        model = CatalogPost
        fields = ( 
            'title',
            'content',
            'category',
            'country',
            'city',
            'site',
            'email',
            'phone',
            'address',
            'skype',
            'google_plus',
            'facebook',
            'twitter',
            'tags',
        )



class ImageUploadForm( forms.ModelForm ):
    post = forms.ModelChoiceField( 
        queryset = CatalogPost.objects.all(),
        widget = forms.HiddenInput()
    )

    class Meta:
        model = CatalogPostImages
