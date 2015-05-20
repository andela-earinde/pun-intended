from django.conf.urls import patterns, include, url
from django.contrib import admin
from issues.views import PostView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pun_int.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^post', view=PostView.as_view())
)
