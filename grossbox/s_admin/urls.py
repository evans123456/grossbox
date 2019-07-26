from django.conf.urls import include,url
from . import views

app_name="s_admin"


urlpatterns = [
	url(r'^$', views.index, name = 'home'),
    url(r'^profile/$', views.profile, name = 'profile'),

]