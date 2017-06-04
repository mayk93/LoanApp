import views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^loans/$', views.LoanList.as_view()),
    url(r'^loan/(?P<pk>[0-9]+)/$', views.LoanDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)