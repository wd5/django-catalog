from django.conf.urls import patterns, include, url

# (?P<year>\d{4})
urlpatterns = patterns( 'catalog',
    url( r'^add/$', 'views.add', name = 'catalog-add' ),
    url( r'^edit/(?P<id>\d+)/$', 'views.edit', name = 'catalog-edit' ),
    url( r'^category-(?P<id>\d+)(?:\-(?P<slug>[\w\-]+))?(?:\/loc\-(?P<country>\d+))?(?:\:(?P<city>\d+))?(?:\/page\-(?P<page>\d+))?', 'views.category', name = 'catalog-category' ),
    url( r'^post-(?P<id>\d+)(?:\-(?P<slug>[\w\-]+))?', 'views.post', name = 'catalog-post' ),
    url( r'^file/$', 'views.file', name = 'catalog-file' ),
    url( r'^ajax/image-upload/$', 'ajax.image_upload', name = 'catalog-ajax-image-upload' ),
    url( r'^ajax/primary/$', 'ajax.primary', name = 'catalog-ajax-primary' ),
    url( r'^(?:loc\-(?P<country>\d+))?(?:\:(?P<city>\d+))?(?:/?page-(?P<page>\d+))?', 'views.home', name = 'catalog-home' ),
 )

