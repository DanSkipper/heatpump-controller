from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'thermal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^remote/', include('remote.urls', namespace='remote')),
    url(r'^schedule/', include('schedule.urls', namespace='schedule')),
    url(r'^admin/', include(admin.site.urls)),
]
