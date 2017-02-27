from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^photoApp/', include('photoApp.urls')),
    url(r'^admin/', admin.site.urls),
]