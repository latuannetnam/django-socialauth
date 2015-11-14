from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^logged/$','socialauth.views.logged'),
    url(r'^logout/$','socialauth.views.logout'),
    url(r'^login/$','socialauth.views.login'),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
