from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.store_list, name='store_list'),
    url(r'^new/$', views.store_create, name='store_create'),
    url(r'^(?P<pk>\d+)/$', views.store_detail, name='store_detail'),
    url(r'^(?P<pk>\d+)/update/$', views.store_update, name='store_update'),
    url(r'^(?P<pk>\d+)/delete/$', views.store_delete, name='store_delete'),
)
