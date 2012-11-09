from django.db import models
from django.conf import settings

from smart_selects.db_fields import ChainedForeignKey

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust

from common.models import CommonCategory, CommonPost
from location.models import Country, City

# Create your models here.

def image_upload_to( instance, filename ):
    filename
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
        format = 'JPEG',
        options = {'quality': 90}
    )
    x50 = ImageSpecField( [
            Adjust( contrast = 1.2, sharpness = 1.1 ),
            ResizeToFill( 50, 50 )
        ],
        image_field = 'image',
        format = 'JPEG',
        options = {'quality': 90}
    )
    thumbnail = ImageSpecField( [
            Adjust( contrast = 1.2, sharpness = 1.1 ),
            ResizeToFill( 150, 150 )
        ],
        image_field = 'image',
        format = 'JPEG',
        options = {'quality': 90}
    )
    x150 = ImageSpecField( [
            Adjust( contrast = 1.2, sharpness = 1.1 ),
            ResizeToFill( 150, 150 )
        ],
        image_field = 'image',
        format = 'JPEG',
        options = {'quality': 90}
    )
    x250 = ImageSpecField( [
            Adjust( contrast = 1.2, sharpness = 1.1 ),
            ResizeToFill( 250, 250 )
        ],
        image_field = 'image',
        format = 'JPEG',
        options = {'quality': 90}
    )
    x450 = ImageSpecField( [
            Adjust( contrast = 1.2, sharpness = 1.1 ),
            ResizeToFill( 450, 450 )
        ],
        image_field = 'image',
        format = 'JPEG',
        options = {
            'quality': 90
        }
    )
    x650 = ImageSpecField( [
            Adjust( contrast = 1.2, sharpness = 1.1 ),
            ResizeToFill( 650, 650 )
        ],
        image_field = 'image',
        format = 'JPEG',
        options = {
            'quality': 90,
            'progressive':True
        }
    )
    description = models.CharField( max_length = 200 )

