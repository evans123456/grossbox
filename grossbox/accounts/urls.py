from django.conf.urls import include,url
from . import views

app_name="accounts"


urlpatterns = [
	url(r'^$', views.index, name = 'home'),
    url(r'^service_application/$', views.registerLaborbusiness , name = 'registerfoodsupply'),
    url(r'^registerfoodsupply/$', views.registerFoodbusiness , name = 'registerfoodsupply'),
    url(r'^registerbiz/$', views.registerbusiness, name = 'registerbusiness'),
    url(r'^biker_registration/$', views.registerbiker, name = 'registerbiker'),
]