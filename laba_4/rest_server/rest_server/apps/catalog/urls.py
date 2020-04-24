from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('game/', views.ComputerGameView.as_view(), name='game'),
    path('game/<int:pk>/', views.ComputerGameIdView.as_view(), name='game_id'),
    path('company/', views.CompanyView.as_view(), name='company'),
    path('company/<int:pk>/', views.CompanyIdView.as_view(), name='company_id'),
    path('platform/', views.PlatformView.as_view(), name='platform'),
    path('platform/<int:pk>/', views.PlatformIdView.as_view(), name='platform_id'),
    path('engine/', views.EngineView.as_view(), name='engine'),
    path('engine/<int:pk>/', views.EngineIdView.as_view(), name='engine_id'),
]
