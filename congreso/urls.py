from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from congress.views import ApplicantViewSet

router = routers.DefaultRouter()
router.register(r'applicants', ApplicantViewSet)
router.register(r'applicants', ApplicantViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'congress.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #rutas de las api
    url(r'^api/', include(router.urls)),
    url(r'^api-auth', include('rest_framework.urls',namespace='rest_framework')),
)
