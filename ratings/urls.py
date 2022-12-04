from django.contrib import admin
from django.urls import path
from ratings import views

urlpatterns = [
    path("", views.index, name='ratings'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
]

