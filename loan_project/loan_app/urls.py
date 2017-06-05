from django.conf.urls import url, include
import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as drf_views

router = DefaultRouter()
router.register(r'loans', views.LoanViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', drf_views.obtain_auth_token),
]