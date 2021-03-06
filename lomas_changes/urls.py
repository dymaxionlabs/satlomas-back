from django.conf.urls import url
from django.urls import include
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register(r'rasters', views.RasterViewSet)
router.register(r'masks', views.MaskViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^download-raster/(?P<pk>[^/]+)$',
        views.RasterDownloadView.as_view()),
    url(r'^coverage/?', views.TimeSeries.as_view()),
    url(r'^available-periods/?', views.AvailablePeriods.as_view()),
]
