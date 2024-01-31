from django.urls import path

from . import views

urlpatterns = [
    path("generate_book", views.generate_book, name="generate_book"),
]
