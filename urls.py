from django.conf.urls import patterns, include, url

# (?P<year>\d{4})
urlpatterns = patterns( 'catalog',
    url( r'^$', 'views.home', name = 'catalog-home' ),
    url( r'^add/$', 'views.add', name = 'catalog-add' ),
    url( r'^edit/(?P<id>\d+)$', 'views.edit', name = 'catalog-edit' ),
    url( r'^category-(?P<id>\d+)(?:\-(?P<slug>[\w\-]+))?', 'views.category', name = 'catalog-category' ),
    url( r'^post-(?P<id>\d+)(?:\-(?P<slug>[\w\-]+))?', 'views.post', name = 'catalog-post' ),
    url( r'^file/$', 'views.file', name = 'catalog-file' ),
 )

