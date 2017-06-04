import views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^loans/$', views.loan_list),
    url(r'^loan/(?P<pk>[0-9]+)/$', views.loan_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)