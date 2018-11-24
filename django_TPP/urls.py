from django.conf.urls import url
from django.contrib import admin

from movies import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('index/', views.index),
]
