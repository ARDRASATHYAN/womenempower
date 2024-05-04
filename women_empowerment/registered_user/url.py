from django.conf.urls import url
from registered_user import views
urlpatterns=[
    url('^reg/',views.reg),
    url('^manage/',views.manage),
    url('^approve/(?P<idd>\w+)',views.approve, name='approve'),
    url('^reject/(?P<idd>\w+)',views.reject, name='reject')




]