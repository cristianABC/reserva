from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<categoria>\w+)/$', views.index, name='index'),
    url(r'^addUser/$', views.add_user_view, name='addUser'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^reload/$', views.reload, name='reload'),
    url(r'^detalle/(?P<especie_id>\d+)/$', views.view_detail, name='detalle'),
    url(r'^editUser/$', views.edit_request, {}, name="editUser"),
    url(r'^addEspecie/$', views.add_especie,name='addEspecie')
]
