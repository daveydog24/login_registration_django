from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^registration$', views.registration),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^clear$', views.clear),
    url(r'^', views.index)
]
