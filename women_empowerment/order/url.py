from django.conf.urls import url
from order import views
urlpatterns=[
    url('^order/(?P<idd>\w+)',views.order, name='order'),
    url('^vieworder/', views.vieworder),
    url('^vieworder/(?P<idd>\w+)',views.vieworder, name='vieworder'),
    url('^manage/', views.manage),
    url('^forwarded/(?P<idd>\w+)',views.forwarded, name='forwarded')
    # url('^accept/(?P<idd>\w+)',views.accept, name='accept'),
    # url('^cancell/(?P<idd>\w+)',views.cancell, name='cancell'),


]