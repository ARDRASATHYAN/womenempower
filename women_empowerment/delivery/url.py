from django.conf.urls import url
from delivery import views
urlpatterns=[
    url('^assign/',views.assign),
    url('^view/',views.view),
    url('^delivery/(?P<idd>\w+)',views.delivery,name='delivery'),

]