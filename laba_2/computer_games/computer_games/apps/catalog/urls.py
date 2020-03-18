from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
	path('', views.index, name='index'),
	path('view/', views.view, name='view'),
	path('edit/', views.edit, name='edit'),
	path('add/', views.add, name='add'),
	path('view/<int:game_id>/', views.view_game, name='view_game'),
	path('edit/<int:game_id>/', views.edit_game, name='edit_game'),
	path('edit/<int:game_id>/game/', views.edit_game_id, name='edit_game_id')
]