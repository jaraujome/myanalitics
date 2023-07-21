from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index),
    path('bar/', views.bar),
    path('pie/', views.pie),
    path('apilada/', views.line),
]

urlpatterns += staticfiles_urlpatterns()

