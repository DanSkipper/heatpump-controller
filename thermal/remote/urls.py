
from django.conf.urls import patterns, url

from remote import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^state/', views.state, name='state'),
)
