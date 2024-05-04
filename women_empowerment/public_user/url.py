from django.conf.urls import url
from public_user import views
urlpatterns=[
    url('^reg/',views.reg),
    # url('^update/', views.update),
    url('^hire/',views.hire , name='hire'),
    url('^labour/',views.labour),
    url('^manage/',views.manage),
    url('update/', views.update, name='update'),
    url('papprove/(?P<idd>\w+)', views.papprove, name='papprove'),
    url('preject/(?P<idd>\w+)', views.preject, name='preject'),






]