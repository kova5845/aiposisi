from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('game/', views.ComputerGameView.as_view(), name='game'),
    path('game/<int:pk>', views.ComputerGameView.as_view(), name='game'),
]
