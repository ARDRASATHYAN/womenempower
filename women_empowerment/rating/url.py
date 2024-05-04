from django.conf.urls import url
from rating import views
urlpatterns=[
    url('^rating/',views.rating),
    url('^viewrating/',views.viewrating),
    url('^viewproduct/',views.viewpr)




]