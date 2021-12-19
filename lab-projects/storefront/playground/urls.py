from django.urls import path
from . import views


#urlConf
urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.sayhello),
    path('hellohtml/', views.passhtmlrender),
]