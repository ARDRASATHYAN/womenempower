from django.conf.urls import url
from product import views
urlpatterns=[
    url('^reg/',views.product),
    url('^manage/', views.manage),
    url('^search/', views.search, ),
    url('^aapprove/(?P<idd>\w+)',views.aapprove, name='aapprove'),
    url('^areject/(?P<idd>\w+)',views.areject, name='areject'),




]