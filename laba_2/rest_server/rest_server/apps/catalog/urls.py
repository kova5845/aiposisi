from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('view/game/', views.ComputerGameView.as_view(), name='view_game'),
]