from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from maps import urls as map_urls
from bizzzzz import urls as business_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'maps/', include((map_urls,'map_urls' ) , namespace = 'maps') ),
    url(r'business/', include((business_urls,'business_urls' ) , namespace = 'business') ),
]
