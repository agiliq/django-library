from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('diglib.views',
    url(r'^$', 'index', name='index')

   )
