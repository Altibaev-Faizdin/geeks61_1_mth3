from django.urls import path
from . import views

urlpatterns = [
    path('All_CARS/', views.relation_db),
]