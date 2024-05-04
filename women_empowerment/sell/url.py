from django.conf.urls import url
from sell import views
urlpatterns=[
    url('^sell/',views.sell),
    url('^remove/(?P<idd>\w+)',views.remove, name='remove'),
    # url('^psell/(?P<idd>\w+)', views.psell, name='psell'),
    url('^productsell/(?P<idd>\w+)',views.productsell, name='productsell'),

]