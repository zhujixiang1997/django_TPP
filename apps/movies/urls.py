from django.conf.urls import url

from movies import views

urlpatterns = [
    url('index/', views.index),
]