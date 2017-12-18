from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new, name='new'),
    url(r'^(?P<user_id>\d+)/edit$', views.edit, name='edit'),
    url(r'^(?P<user_id>\d+)$', views.show, name='show'),
    url(r'^create$', views.create, name='create'),
    url(r'^(?P<user_id>\d+)/destroy$', views.destroy, name='destroy'),
    url(r'^update$', views.update, name='update')
]
