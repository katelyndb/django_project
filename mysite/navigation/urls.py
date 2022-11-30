from django.urls import path
from navigation import views
from languages import views
from home import views
from hello import views

# Create your views here.

urlpatterns = [
    path("", views.index, name="index"),

    
    path('hello/', views.hello, name='hello'),
    path("tutorial/", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("index/", views.index, name="index"),
    path("language/", views.language_list, name="language_list"),
    path("<int:pk>/", views.language_detail, name="language_detail"),
]
