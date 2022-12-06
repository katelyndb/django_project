from django.urls import path
from cats import views

urlpatterns = [
    path("", views.cats, name="cats"),
] 