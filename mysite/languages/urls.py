from django.urls import path
from languages import views

# Create your views here.

urlpatterns = [
    path("", views.index, name="index"),
    path("language/", views.language_list, name="language_list"),
    path("<int:pk>/", views.language_detail, name="language_detail"),
    
]
