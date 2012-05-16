from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('diglib.views', 
    url(r'^detail/(?P<var_name>\w+)/(?P<var_id>\d+)/$', 'detail', name='detail'),
    url(r'^$', 'index', name='index'),
    url(r'^$', 'status', name='status')
)

