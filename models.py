from django.db import models
from django.conf import settings

import uuid

from smart_selects.db_fields import ChainedForeignKey

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust, SmartResize, ResizeToFit

from common.models import CommonCategory, CommonPost
from location.models import Country, City

# Create your models here.

def image_upload_to( instance, filename ):
    ext = filename.split( '.' )[-1]
    filename = "%s.%s" % ( uuid.uuid4(), ext.lower() )
    return 'catalog/%s/%s' % ( instance.post.id, filename )


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


class CatalogPostImages( models.Model ):
    post = models.ForeignKey( CatalogPost, default = '', blank = True, null = True, )
    image = models.ImageField( upload_to = image_upload_to )
    icon = ImageSpecField( [
            Adjust( contrast = 1.2, sharpness = 1.1 ),
            ResizeToFill( 50, 50 )
        ],
        image_field = 'image',
#        format = 'JPEG',
        options = {
            'quality': 90,
            'progressive':True,
        }
    )
    x50 = ImageSpecField( [
            Adjust( contrast = 1.2, sharpness = 1.1 ),
            ResizeToFit( 50, 50 )
        ],
        image_field = 'image',
#        format = 'JPEG',
        options = {
            'quality': 90,
            'progressive':True,
        }
    )
    x100 = ImageSpecField( [
            Adjust( contrast = 1.2, sharpness = 1.1 ),
            ResizeToFit( 100, 100 )
        ],
        image_field = 'image',
#        format = 'JPEG',
        options = {
            'quality': 90,
            'progressive':True,
        }
    )
    thumbnail = ImageSpecField( [
            Adjust( contrast = 1.2, sharpness = 1.1 ),
            ResizeToFit( 150, 150 )
        ],
        image_field = 'image',
#        format = 'JPEG',
        options = {
            'quality': 90,
            'progressive':True,
        }
    )
    x150 = ImageSpecField( [
            Adjust( contrast = 1.2, sharpness = 1.1 ),
            ResizeToFit( 150, 150 )
        ],
        image_field = 'image',
        options = {
            'quality': 90,
            'progressive':True,
        }
    )
    x250 = ImageSpecField( [
            Adjust( contrast = 1.2, sharpness = 1.1 ),
            ResizeToFit( 250, 250 )
        ],
        image_field = 'image',
#        format = 'JPEG',
        options = {
            'quality': 90,
            'progressive':True,
        }
    )
    x450 = ImageSpecField( [
            Adjust( contrast = 1.2, sharpness = 1.1 ),
            ResizeToFit( 450, 450 )
        ],
        image_field = 'image',
#        format = 'JPEG',
        options = {
            'quality': 90,
            'progressive':True,
        }
    )
    x650 = ImageSpecField( [
            Adjust( contrast = 1.2, sharpness = 1.1 ),
            ResizeToFit( 650, 650 )
        ],
        image_field = 'image',
#        format = 'JPEG',
        options = {
            'quality': 90,
            'progressive':True,
        }
    )
    description = models.CharField( max_length = 200, blank = True, )

