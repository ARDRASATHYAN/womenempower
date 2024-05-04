from django.conf.urls import url
from sales_report import views
urlpatterns=[
    url('^report/',views.report),
    url('^salereport/', views.salereport),





]