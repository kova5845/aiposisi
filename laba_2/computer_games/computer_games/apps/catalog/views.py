from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import ComputerGame, Company, Platform, Engine
from django.urls import reverse
from datetime import datetime


def index(request):
	return render(request, 'base.html')


def view_game(request):
	game_list = ComputerGame.objects.all()
	return render(request, 'catalog/view_game.html', {'game_list': game_list})


def add_game(request):
	return render(request, 'catalog/add_game.html')


def add_game_game(request):
	try:
		game = ComputerGame()
		game.name = request.POST['name']
		game.genre = request.POST['genre']
		game.setting = request.POST['setting']
		game.date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
		game.save()
	except:
		raise Http404('Игра не создана')

	return HttpResponseRedirect(reverse('catalog:view_game'))


def view_game_id(request, game_id):
	try:
		game = ComputerGame.objects.get(id=game_id)
	except:
		raise Http404('Игра не найдена')

	return render(request, 'catalog/view_game_id.html', {'game': game})


def edit_game_id(request, game_id):
	try:
		game = ComputerGame.objects.get(id=game_id)
	except:
		raise Http404('Игра не найдена')

	return render(request, 'catalog/edit_game_id.html', {'game': game, 'game_date': game.date.strftime('%Y-%m-%d')})


def edit_game_id_edit(request, game_id):
	try:
		game = ComputerGame.objects.get(id=game_id)
		game.name = request.POST['name']
		game.genre = request.POST['genre']
		game.setting = request.POST['setting']
		game.date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
		game.save()
	except:
		raise Http404('Игра не найдена')

	return HttpResponseRedirect(reverse('catalog:view_game'))


def delete_game_id(request, game_id):
	try:
		game = ComputerGame.objects.get(id=game_id)
		game.delete()
	except:
		raise Http404('Игра не найдена')

	return HttpResponseRedirect(reverse('catalog:view_game'))


def view_company(request):
	company_list = Company.objects.all()
	return render(request, 'catalog/view_company.html', {'company_list': company_list})


def view_company_id(request, company_id):
	try:
		company = Company.objects.get(id=company_id)
	except:
		raise Http404('Компания не найдена')

	return render(request, 'catalog/view_company_id.html', {'company': company})


def add_company(request):
	return render(request, 'catalog/add_company.html')


def add_company_company(request):
	try:
		company = Company()
		company.name = request.POST['name']
		company.place = request.POST['place']
		company.date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
		company.save()
	except:
		raise Http404('Игра не создана')

	return HttpResponseRedirect(reverse('catalog:view_company'))


def edit_company_id(request, company_id):
	try:
		company = Company.objects.get(id=company_id)
	except:
		raise Http404('Игра не найдена')

	return render(request, 'catalog/edit_company_id.html',
		{'company': company, 'company_date': company.date.strftime('%Y-%m-%d')})


def edit_company_id_edit(request, company_id):
	try:
		company = Company.objects.get(id=company_id)
		company.name = request.POST['name']
		company.place = request.POST['place']
		company.date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
		company.save()
	except:
		raise Http404('Игра не найдена')

	return HttpResponseRedirect(reverse('catalog:view_company'))


def delete_company_id(request, company_id):
	try:
		company = Company.objects.get(id=company_id)
		company.delete()
	except:
		raise Http404('Игра не найдена')

	return HttpResponseRedirect(reverse('catalog:view_company'))


def view_platform(request):
	platform_list = Platform.objects.all()
	return render(request, 'catalog/view_platform.html', {'platform_list': platform_list})


def view_platform_id(request, platform_id):
	try:
		platform = Platform.objects.get(id=platform_id)
	except:
		raise Http404('Компания не найдена')

	return render(request, 'catalog/view_platform_id.html', {'platform': platform})


def add_platform(request):
	return render(request, 'catalog/add_platform.html')


def add_platform_platform(request):
	try:
		platform = Platform()
		platform.name = request.POST['name']
		platform.date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
		platform.save()
	except:
		raise Http404('Игра не создана')

	return HttpResponseRedirect(reverse('catalog:view_platform'))


def edit_platform_id(request, platform_id):
	try:
		platform = Platform.objects.get(id=platform_id)
	except:
		raise Http404('Игра не найдена')

	return render(request, 'catalog/edit_platform_id.html',
		{'platform': platform, 'platform_date': platform.date.strftime('%Y-%m-%d')})


def edit_platform_id_edit(request, platform_id):
	try:
		platform = Platform.objects.get(id=platform_id)
		platform.name = request.POST['name']
		platform.date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
		platform.save()
	except:
		raise Http404('Игра не найдена')

	return HttpResponseRedirect(reverse('catalog:view_platform'))


def delete_platform_id(request, platform_id):
	try:
		platform = Platform.objects.get(id=platform_id)
		platform.delete()
	except:
		raise Http404('Игра не найдена')

	return HttpResponseRedirect(reverse('catalog:view_platform'))






def view_engine(request):
	engine_list = Engine.objects.all()
	return render(request, 'catalog/view_engine.html', {'engine_list': engine_list})


def view_engine_id(request, engine_id):
	try:
		engine = Engine.objects.get(id=engine_id)
	except:
		raise Http404('Компания не найдена')

	return render(request, 'catalog/view_engine_id.html', {'engine': engine})


def add_engine(request):
	return render(request, 'catalog/add_engine.html')


def add_engine_engine(request):
	try:
		engine = Engine()
		engine.name = request.POST['name']
		engine.language = request.POST['language']
		engine.date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
		engine.save()
	except:
		raise Http404('Игра не создана')

	return HttpResponseRedirect(reverse('catalog:view_engine'))


def edit_engine_id(request, engine_id):
	try:
		engine = Engine.objects.get(id=engine_id)
	except:
		raise Http404('Игра не найдена')

	return render(request, 'catalog/edit_engine_id.html',
		{'engine': engine, 'engine_date': engine.date.strftime('%Y-%m-%d')})


def edit_engine_id_edit(request, engine_id):
	try:
		engine = Engine.objects.get(id=engine_id)
		engine.name = request.POST['name']
		engine.language = request.POST['language']
		engine.date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
		engine.save()
	except:
		raise Http404('Игра не найдена')

	return HttpResponseRedirect(reverse('catalog:view_engine'))


def delete_engine_id(request, engine_id):
	try:
		engine = Engine.objects.get(id=engine_id)
		engine.delete()
	except:
		raise Http404('Игра не найдена')

	return HttpResponseRedirect(reverse('catalog:view_engine'))
