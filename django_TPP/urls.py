from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url('admin/', admin.site.urls),
    url('shouye/', include('apps.movies.urls')),
]
