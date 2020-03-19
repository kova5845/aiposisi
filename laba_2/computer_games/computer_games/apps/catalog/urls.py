from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
	path('', views.index, name='index'),

	path('view/game/', views.view_game, name='view_game'),
	path('add/game/', views.add_game, name='add_game'),
	path('add/game/game/', views.add_game_game, name='add_game_game'),
	path('view/game/<int:game_id>/', views.view_game_id, name='view_game_id'),
	path('edit/game/<int:game_id>/', views.edit_game_id, name='edit_game_id'),
	path('edit/game/<int:game_id>/edit/', views.edit_game_id_edit, name='edit_game_id_edit'),
	path('delete/game/<int:game_id>/', views.delete_game_id, name='delete_game_id'),

	path('view/company/', views.view_company, name='view_company'),
	path('add/company/', views.add_company, name='add_company'),
	path('add/company/company', views.add_company_company, name='add_company_company'),
	path('view/company/<int:company_id>/', views.view_company_id, name='view_company_id'),
	path('edit/company/<int:company_id>/', views.edit_company_id, name='edit_company_id'),
	path('edit/company/<int:company_id>/edit/', views.edit_company_id_edit, name='edit_company_id_edit'),
	path('delete/company/<int:company_id>/', views.delete_company_id, name='delete_company_id'),

	path('view/platform/', views.view_platform, name='view_platform'),
	path('add/platform/', views.add_platform, name='add_platform'),
	path('add/platform/platform', views.add_platform_platform, name='add_platform_platform'),
	path('view/platform/<int:platform_id>/', views.view_platform_id, name='view_platform_id'),
	path('edit/platform/<int:platform_id>/', views.edit_platform_id, name='edit_platform_id'),
	path('edit/platform/<int:platform_id>/edit/', views.edit_platform_id_edit, name='edit_platform_id_edit'),
	path('delete/platform/<int:platform_id>/', views.delete_platform_id, name='delete_platform_id'),

	path('view/engine/', views.view_engine, name='view_engine'),
	path('add/engine/', views.add_engine, name='add_engine'),
	path('add/engine/engine', views.add_engine_engine, name='add_engine_engine'),
	path('view/engine/<int:engine_id>/', views.view_engine_id, name='view_engine_id'),
	path('edit/engine/<int:engine_id>/', views.edit_engine_id, name='edit_engine_id'),
	path('edit/engine/<int:engine_id>/edit/', views.edit_engine_id_edit, name='edit_engine_id_edit'),
	path('delete/engine/<int:engine_id>/', views.delete_engine_id, name='delete_engine_id'),
]
