from django.contrib import admin


from common.admin import CommonPostAdmin, CommonCategooryAdmin
from . models import CatalogCategory, CatalogPost

class CatalogCategoryAdmin( CommonCategooryAdmin ):
    pass

class CatalogPostAdmin( CommonPostAdmin ):
    list_display = ( 'title', 'author', 'date_edit', 'date_add', 'status', 'country', 'city', )

admin.site.register( CatalogCategory, CatalogCategoryAdmin )
admin.site.register( CatalogPost, CatalogPostAdmin )
