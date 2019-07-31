from django.conf.urls import include,url
from . import views
from django.contrib.auth.views import LoginView

app_name="accounts"


urlpatterns = [
	url(r'^$', views.index, name = 'home'),
    url(r'^service_application/$', views.registerLaborbusiness , name = 'service_application'),
    url(r'^registerfoodsupply/$', views.registerFoodbusiness , name = 'registerfoodsupply'),
    url(r'^registerbiz/$', views.registerbusiness, name = 'registerbusiness'),
    url(r'^biker_registration/$', views.registerbiker, name = 'registerbiker'),
    url(r'^signup-select/$', views.selection, name = 'selection'),
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name='login')

]