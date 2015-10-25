from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'backdoor_central_web.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', 'backdoor_central_web.views.login', name="login"),
    url(r'^logout/$', 'backdoor_central_web.views.logout', name="logout"),
    url(r'^virtual_machine_selection/$', 'backdoor_central_web.views.virtual_machine_selection', name="virtual_machine_selection"),
    url(r'^index/$', 'backdoor_central_web.views.index', name="index"),
    url(r'^login/authenticate/$', 'backdoor_central_web.views.authenticate', name="authenticate"),
    url(r'^ajax_handler/(?P<action>.+)/', 'backdoor_central_web.views.ajax_handler', name='ajax_handler'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
