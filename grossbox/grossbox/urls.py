from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from maps import urls as map_urls
from bizzzzz import urls as business_urls
from accounts import urls as accounts_urls
from s_admin import urls as superadmin_urls
from bikers import urls as bikers_urls
from home import urls as home_urls



urlpatterns = [
    path('super_admin/', admin.site.urls),
    url(r'', include((home_urls,'home_urls' ) , namespace = 'homepage') ),
    url(r'maps/', include((map_urls,'map_urls' ) , namespace = 'maps') ),
    url(r'business/', include((business_urls,'business_urls' ) , namespace = 'business') ),
    url(r'accounts/', include((accounts_urls,'accounts_urls' ) , namespace = 'accounts') ),
    url(r'useradministration/', include((superadmin_urls,'superadmin_urls' ) , namespace = 'superadmin_urls') ),
    url(r'bikers/', include((bikers_urls,'bikers_urls' ) , namespace = 'bikers') ),
]
