from rest_framework_nested import routers

from django.conf.urls import patterns, url, include

from authentication.views import AccountViewSet
from authentication.views import LoginView
from .views import IndexView

router = routers.SimpleRouter()

router.register(r'accounts', AccountViewSet)

urlpatterns = patterns(
    '',
    url('^', include(router.urls)),
    url(r'^/auth/login/$', LoginView.as_view(), name='login'),    
    url('^.*$', IndexView.as_view(), name='index'),
)
