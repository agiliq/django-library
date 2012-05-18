from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('diglib.views', 
    url(r'^detail/(?P<var_name>\w+)/(?P<var_id>\d+)/$', 'detail', name='detail'),
    url(r'^filter/books/(?P<var_name>\w+)/(?P<var_id>\d+)/$', 'filter', name='filter'),        url(r'^accounts/login/$', 'aclogin', name='aclogin'),
    url(r'^accounts/logout/$', 'aclogout', name='aclogout'),
    url(r'^(?P<book_id>\d+)/(?P<var>\w+)/$', 'funct', name='funct'),
    url(r'^libdetails/$', 'libdetails', name='libdetails'), 
    url(r'^request/(?P<var>\w+)/$', 'book_request', name='book_request'),
    url(r'^request/edit/(?P<req_id>\d+)/$', 'edit_request', name='edit_request'),
    url(r'^$', 'index', name='index'),
    url(r'^about/$', 'about', name='about')
)

