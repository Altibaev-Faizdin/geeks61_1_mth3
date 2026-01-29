from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.helo_world_view),
]