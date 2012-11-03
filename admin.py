from django.contrib import admin


from common.admin import CommonPostAdmin, CommonCategooryAdmin
from . models import CatalogCategory, CatalogPost

class CategoryAdmin( CommonCategooryAdmin ):
    pass

class PostAdmin( CommonPostAdmin ):
    list_display = ( 'title', 'author', 'date_edit', 'date_add', 'status', 'country', 'city', )

admin.site.register( CatalogCategory, CategoryAdmin )
admin.site.register( CatalogPost, PostAdmin )
