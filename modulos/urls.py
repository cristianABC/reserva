from django.conf.urls import url
from . import views

urlpatterns= [
     url(r'^$',views.index,name='index'),
     url(r'^addUser/$', views.add_user_view, name='addUser'),
     url(r'^login/$', views.login_view, name='login'),
     url(r'^logout/$', views.login_view, name='logout'),

]