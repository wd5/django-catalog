from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple


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


class ImageUploadForm( forms.ModelForm ):
    post = forms.ModelChoiceField( 
        queryset = CatalogPost.objects.all(),
        widget = forms.HiddenInput()
    )
    class Meta:
        model = CatalogPostImages
#        fields = ( 'image', 'description' )
#    title = forms.CharField( max_length = 50 )
#    file = forms.ImageField()
