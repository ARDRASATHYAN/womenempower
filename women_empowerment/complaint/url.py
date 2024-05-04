from django.conf.urls import url
from complaint import views
urlpatterns=[
    url('^postcmp/',views.postcmp),
    url('^viewcmp/',views.viewcmp),
    # url('^postreply/',views.postreply),
    url('^viewreply/',views.viewreply),
    url('^postreply/(?P<idd>\w+)',views.postreply, name='postreply')

]