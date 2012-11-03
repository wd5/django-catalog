from django.db import models
from django.conf import settings

from smart_selects.db_fields import ChainedForeignKey

from common.models import CommonCategory, CommonPost
from location.models import Country, City

# Create your models here.

class CatalogCategory( CommonCategory ):
    pass

class CatalogPost( CommonPost ):
    category = models.ManyToManyField( CatalogCategory )
    country = models.ForeignKey( Country, blank = True, null = True, )
    city = ChainedForeignKey( 
        City,
        chained_field = "country",
        chained_model_field = "country",
        show_all = False,
        auto_choose = False
    )
#    city = models.ForeignKey( City, blank = True, null = True, )


#class PostImages( models.Model ):
#    post = models.ForeignKey( Post )
#    image = models.ImageField(
#        upload_to = settings.APPPATH + 'catalog/uploads/'
#    )
#    description = models.CharField( max_length = 200 )
