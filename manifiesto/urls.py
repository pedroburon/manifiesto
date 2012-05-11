from django.conf.urls import patterns, include, url
from django.views.generic import ListView

from signers.models import Signer

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'manifiesto.views.home', name='home'),
    # url(r'^manifiesto/', include('manifiesto.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

   url(r'^signers/', ListView.as_view(model=Signer), 
       name='signer_list'),
)
