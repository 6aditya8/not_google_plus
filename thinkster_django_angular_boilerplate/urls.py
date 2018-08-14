from rest_framework_nested import routers

from django.conf.urls import patterns, url, include

from authentication.views import AccountViewSet
from .views import IndexView

router = routers.SimpleRouter()

router.register(r'accounts', AccountViewSet)

urlpatterns = patterns(
    '',
    url('^', include(router.urls)),
    url('^.*$', IndexView.as_view(), name='index'),
)
