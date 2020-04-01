from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import ComputerGame, Company, Platform, Engine
from django.urls import reverse
from datetime import datetime


def index(request):
	print('Main menu')
	return render(request, 'catalog/main.html')


def view_game(request):
	print('Game list')
	my_list = ComputerGame.objects.all()
	paginator = Paginator(my_list, 5)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)
	return render(request, 'catalog/view_game.html', {'contacts': contacts})


def add_game(request):
	print('Add game')
	company = Company.objects.all()
	platform = Platform.objects.all()
	engine = Engine.objects.all()
	return render(request, 'catalog/add_game.html', {
		'company': company,
		'platform': platform,
		'engine': engine
	})


def add_game_game(request, game_id=None):
	if game_id is None:
		game = ComputerGame()
	else:
		game = ComputerGame.objects.get(id=game_id)
	game.name = request.POST['name']
	game.genre = request.POST['genre']
	game.setting = request.POST['setting']
	game.date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
	game.save()
	platform = []
	for pl in request.POST.getlist('platform'):
		platform.append(Platform.objects.get(name=pl))
	game.platform.clear()
	for pl in platform:
		game.platform.add(pl)
	company = Company.objects.get(name=request.POST['company'])
	game.company = company
	engine = Engine.objects.get(name=request.POST['engine'])
	game.engine = engine
	game.save()
	return HttpResponseRedirect(reverse('catalog:view_game'))


def view_game_id(request, game_id):
	game = ComputerGame.objects.get(id=game_id)
	print('View {0}'.format(game.name))
	return render(request, 'catalog/view_game_id.html', {'game': game})


def edit_game_id(request, game_id):
	game = ComputerGame.objects.get(id=game_id)
	print('Edit {0}'.format(game.name))
	company = Company.objects.all()
	platform = Platform.objects.all()
	engine = Engine.objects.all()
	return render(request, 'catalog/edit_game_id.html', {
		'game': game,
		'game_date': game.date.strftime('%Y-%m-%d'),
		'company': company,
		'platform': platform,
		'engine': engine
	})


def edit_game_id_edit(request, game_id):
	return add_game_game(request, game_id)


def delete_game_id(request, game_id):
	game = ComputerGame.objects.get(id=game_id)
	print('Delete {0}'.format(game.name))
	game.delete()
	return HttpResponseRedirect(reverse('catalog:view_game'))


def view_company(request):
	print('Company list')
	my_list = Company.objects.all()
	paginator = Paginator(my_list, 5)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)
	return render(request, 'catalog/view_company.html', {'contacts': contacts})


def view_company_id(request, company_id):
	company = Company.objects.get(id=company_id)
	print('View {0}'.format(company.name))
	return render(request, 'catalog/view_company_id.html', {'company': company})


def add_company(request):
	print('Add company')
	return render(request, 'catalog/add_company.html')


def add_company_company(request, company_id=None):
	if company_id is None:
		company = Company()
	else:
		company = Company.objects.get(id=company_id)
	company.name = request.POST['name']
	company.place = request.POST['place']
	company.date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
	company.save()
	return HttpResponseRedirect(reverse('catalog:view_company'))


def edit_company_id(request, company_id):
	company = Company.objects.get(id=company_id)
	print('Edit {0}'.format(company.name))
	return render(request, 'catalog/edit_company_id.html', {
		'company': company,
		'company_date': company.date.strftime('%Y-%m-%d')
	})


def edit_company_id_edit(request, company_id):
	return add_company_company(request, company_id)


def delete_company_id(request, company_id):
	company = Company.objects.get(id=company_id)
	print('View {0}'.format(company.name))
	company.delete()
	return HttpResponseRedirect(reverse('catalog:view_company'))


def view_platform(request):
	print('Platform list')
	my_list = Platform.objects.all()
	paginator = Paginator(my_list, 5)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)
	return render(request, 'catalog/view_platform.html', {'contacts': contacts})


def view_platform_id(request, platform_id):
	platform = Platform.objects.get(id=platform_id)
	print('View {0}'.format(platform.name))
	return render(request, 'catalog/view_platform_id.html', {'platform': platform})


def add_platform(request):
	print('Add platform')
	company = Company.objects.all()
	game = ComputerGame.objects.all()
	return render(request, 'catalog/add_platform.html',  {
		'company': company,
		'game': game
	})


def add_platform_platform(request, platform_id=None):
	if platform_id is None:
		platform = Platform()
	else:
		platform = Platform.objects.get(id=platform_id)
	platform.name = request.POST['name']
	platform.date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
	platform.save()
	company = Company.objects.get(name=request.POST['company'])
	platform.company = company
	platform.save()
	return HttpResponseRedirect(reverse('catalog:view_platform'))


def edit_platform_id(request, platform_id):
	platform = Platform.objects.get(id=platform_id)
	print('Edit {0}'.format(platform.name))
	company = Company.objects.all()
	game = ComputerGame.objects.all()
	return render(request, 'catalog/edit_platform_id.html',	{
		'platform': platform,
		'platform_date': platform.date.strftime('%Y-%m-%d'),
		'company': company,
		'game': game
	})


def edit_platform_id_edit(request, platform_id):
	return add_platform_platform(request, platform_id)


def delete_platform_id(request, platform_id):
	platform = Platform.objects.get(id=platform_id)
	print('View {0}'.format(platform.name))
	platform.delete()
	return HttpResponseRedirect(reverse('catalog:view_platform'))


def view_engine(request):
	print('Engine list')
	my_list = Engine.objects.all()
	paginator = Paginator(my_list, 5)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)
	return render(request, 'catalog/view_engine.html', {'contacts': contacts})


def view_engine_id(request, engine_id):
	engine = Engine.objects.get(id=engine_id)
	print('View {0}'.format(engine.name))
	return render(request, 'catalog/view_engine_id.html', {'engine': engine})


def add_engine(request):
	print('Add engine')
	company = Company.objects.all()
	return render(request, 'catalog/add_engine.html', {'company': company})


def add_engine_engine(request, engine_id=None):
	if engine_id is None:
		engine = Engine()
	else:
		engine = Engine.objects.get(id=engine_id)
	engine.name = request.POST['name']
	engine.language = request.POST['language']
	engine.date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
	engine.save()
	company = Company.objects.get(name=request.POST['company'])
	engine.company = company
	engine.save()
	return HttpResponseRedirect(reverse('catalog:view_engine'))


def edit_engine_id(request, engine_id):
	engine = Engine.objects.get(id=engine_id)
	print('Edit {0}'.format(engine.name))
	company = Company.objects.all()
	return render(request, 'catalog/edit_engine_id.html', {
		'engine': engine,
		'engine_date': engine.date.strftime('%Y-%m-%d'),
		'company': company
	})


def edit_engine_id_edit(request, engine_id):
	return add_engine_engine(request, engine_id)


def delete_engine_id(request, engine_id):
	engine = Engine.objects.get(id=engine_id)
	print('View {0}'.format(engine.name))
	engine.delete()
	return HttpResponseRedirect(reverse('catalog:view_engine'))
