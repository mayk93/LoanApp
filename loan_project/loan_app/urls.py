from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
import views

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^loans/$',
        views.LoanList.as_view(),
        name='loan-list'),
    url(r'^loans/(?P<pk>[0-9]+)/$',
        views.LoanDetail.as_view(),
        name='loan-detail'),
    url(r'^loans/(?P<pk>[0-9]+)/synopsis/$',
        views.LoanSynopsis.as_view(),
        name='loan-synopsis'),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail')
])

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]