from django.conf.urls import url
import views

urlpatterns = [
    url(r'^loans/$', views.loan_list),
    url(r'^loan/(?P<pk>[0-9]+)/$', views.loan_detail),
]