from django.urls import path
from django.contrib import admin
from . import views

admin.site.site_header = "Explore With Us Portal"
admin.site.site_title = "Welcome to Explore With Us Dashboard"
admin.site.index_title = "Welcome to the Portal"
urlpatterns = [
    # Path converters
    # int: numbers
    # str: strings
    # path: whole urls /
    # slug: hyphen-and_underscore_stuff
    # UUID: universally unique identifier like username
    path('', views.index),
    path('subscribe', views.sub, name='sub'),
    path('search/', views.search),
    path('dests/<str:destname>', views.result),

]

