from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers

from views import LoanViewSet, UserViewSet, api_root

loan_list = LoanViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
loan_detail = LoanViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
loan_synopsis = LoanViewSet.as_view({
    'get': 'synopsis'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^loans/$', loan_list, name='loan-list'),
    url(r'^loans/(?P<pk>[0-9]+)/$', loan_detail, name='loan-detail'),
    url(r'^loans/(?P<pk>[0-9]+)/synopsis/$', loan_synopsis, name='loan-synopsis'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
])