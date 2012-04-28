from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('agibrary.diglib.urls')),

     # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

                   
)
