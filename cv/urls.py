from django import urls
from django.urls import path
from . import views
urlpatterns=[
    path('portfolio/',views.index,name="portfolio")
]