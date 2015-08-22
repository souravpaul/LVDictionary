from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LVDictionary.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'dictionary.views.index', name='index'),
    url(r'^bookmark/create/', 'dictionary.views.bookmark', name='bookmark'),
    url(r'^bookmark/check/', 'dictionary.views.bookmarkCheck', name='bookmark'),
    url(r'^bookmark/clear/', 'dictionary.views.bookmarkremove', name='bookmarkremove'),
)
