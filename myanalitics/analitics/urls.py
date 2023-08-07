from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index),
    path('bar/', views.bar, name='bar'),
    path('pie/', views.pie, name='pie'),
    path('apilada/', views.line, name='apilada'),
]

urlpatterns += staticfiles_urlpatterns()

