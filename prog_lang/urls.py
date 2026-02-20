from django.urls import path
from . import views

app_name = 'yaziki'

urlpatterns = [
    path('prog_lang/', views.ProgLangListView.as_view(), name='yaziki_programm'),
    path('prog_lang/<int:id>/', views.ProgLangDetailView.as_view(), name='prog_lang_detail'),

    path('create_prog_lang/', views.CreateProgLangView.as_view(), name='create_prog_lang'),

    path('prog_lang/<int:id>/delete', views.DeleteProgLangView.as_view()),
    path('prog_lang/<int:id>/update/', views.UpdateProgLangView.as_view()),


    path('search/', views.SeachView.as_view()),
]


