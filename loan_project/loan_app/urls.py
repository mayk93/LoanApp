from django.conf.urls import url, include
import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'loans', views.LoanViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]