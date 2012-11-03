from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple


from common.forms import CommonPostEditForm
from . models import Post, Category

class CatalogEditForm( CommonPostEditForm ):
    category = forms.ModelMultipleChoiceField( 
        queryset = Category.objects.all(),
        required = False,
        widget = FilteredSelectMultiple( 
            'categories',
            False,
        )
    )

    class Meta( CommonPostEditForm.Meta ):
        model = Post
