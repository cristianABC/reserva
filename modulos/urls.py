from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addUser/$', views.add_user_view, name='addUser'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^reload/$', views.reload, name='reload'),
    url(r'^detalle/(?P<especie_id>\d+)/$', views.view_detail, name='detalle'),
    url(r'^editUser/$', views.edit_request, {}, name="editUser"),
    url(r'^addEspecie/$', views.add_especie, name='addEspecie'),
    url(r'^detalle/(?P<especie_id>\d+)/addComentario', views.add_comment, name='addComentario'),
    # REST
    url(r'^rest/all/$', views.get_all_species, name='rest/all'),
    url(r'^rest/(?P<especie_id>\d+)/', views.search_specie, name='rest/search'),
    url(r'^rest/(?P<categoria>\w+)/', views.search_type, name='rest/searchType'),

]
