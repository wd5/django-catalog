from django.db import models
from django.conf import settings

import uuid

from smart_selects.db_fields import ChainedForeignKey

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust, SmartResize, ResizeToFit

from common.models import CommonCategory, CommonPost, CommonPostImage
from location.models import Country, City

# Create your models here.

def image_upload_to( instance, filename ):
    ext = filename.split( '.' )[-1]
    filename = "%s.%s" % ( uuid.uuid4(), ext.lower() )
    id = str( instance.post.id )
    return 'catalog/%s/%s/%s' % ( id[:1], id, filename )

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


class CatalogPostImages( CommonPostImage ):
    post = models.ForeignKey( CatalogPost, default = '', blank = True, null = True, )
    image = models.ImageField( upload_to = image_upload_to )
