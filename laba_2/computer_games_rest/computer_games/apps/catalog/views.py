from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.urls import reverse
import requests

PORT = '5000'


def index(request):
	print('Main menu')
	return render(request, 'catalog/main.html')


def view_game(request):
	print('Game list')
	my_list = requests.get('http://localhost:{0}/catalog/game/'.format(PORT)).json()
	paginator = Paginator(my_list['game'], 5)
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
	company = requests.get('http://localhost:{0}/catalog/company/'.format(PORT)).json()['company']
	platform = requests.get('http://localhost:{0}/catalog/platform/'.format(PORT)).json()['platform']
	engine = requests.get('http://localhost:{0}/catalog/engine/'.format(PORT)).json()['engine']
	return render(request, 'catalog/add_game.html', {
		'company': company,
		'platform': platform,
		'engine': engine
	})


def add_game_game(request, game_id=None):
	if game_id is None:
		game = {
			"game": {}
		}
	else:
		game = requests.get('http://localhost:{0}/catalog/game/{1}/'.format(PORT, game_id)).json()
	game['game']['name'] = request.POST['name']
	game['game']['genre'] = request.POST['genre']
	game['game']['setting'] = request.POST['setting']
	game['game']['date'] = request.POST['date']
	game['game']['company'] = int(request.POST['company'])
	game['game']['engine'] = int(request.POST['engine'])
	platform = []
	for pl in request.POST.getlist('platform'):
		platform.append(int(pl))
	game['game']['platform'] = platform
	if game_id is None:
		requests.post('http://localhost:{0}/catalog/game/'.format(PORT), json=game)
	else:
		requests.put('http://localhost:{0}/catalog/game/{1}/'.format(PORT, game['game']['id']), json=game)
	return HttpResponseRedirect(reverse('catalog:view_game'))


def view_game_id(request, game_id):
	game = requests.get('http://localhost:{0}/catalog/game/{1}/'.format(PORT, game_id)).json()['game']
	print('View {0}'.format(game['name']))
	company = requests.get('http://localhost:{0}/catalog/company/{1}/'.format(PORT, game['company'])).json()['company']
	engine = requests.get('http://localhost:{0}/catalog/engine/{1}/'.format(PORT, game['engine'])).json()['engine']
	platform = []
	for pl in game['platform']:
		platform.append(requests.get('http://localhost:{0}/catalog/platform/{1}/'.format(PORT, pl)).json()['platform'])
	return render(request, 'catalog/view_game_id.html', {
		'game': game,
		'company': company,
		'engine': engine,
		'platform': platform,
	})


def edit_game_id(request, game_id):
	game = requests.get('http://localhost:{0}/catalog/game/{1}/'.format(PORT, game_id)).json()['game']
	print('Edit {0}'.format(game['name']))
	company = requests.get('http://localhost:{0}/catalog/company/'.format(PORT)).json()['company']
	platform = requests.get('http://localhost:{0}/catalog/platform/'.format(PORT)).json()['platform']
	engine = requests.get('http://localhost:{0}/catalog/engine/'.format(PORT)).json()['engine']
	return render(request, 'catalog/edit_game_id.html', {
		'game': game,
		'company': company,
		'platform': platform,
		'engine': engine
	})


def edit_game_id_edit(request, game_id):
	return add_game_game(request, game_id)


def delete_game_id(request, game_id):
	game = requests.get('http://localhost:{0}/catalog/game/{1}/'.format(PORT, game_id)).json()['game']
	requests.delete('http://localhost:{0}/catalog/game/{1}/'.format(PORT, game_id))
	print('Delete {0}'.format(game['name']))
	return HttpResponseRedirect(reverse('catalog:view_game'))


def view_company(request):
	print('Company list')
	my_list = requests.get('http://localhost:{0}/catalog/company/'.format(PORT)).json()
	paginator = Paginator(my_list['company'], 5)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)
	return render(request, 'catalog/view_company.html', {'contacts': contacts})


def view_company_id(request, company_id):
	company = requests.get('http://localhost:{0}/catalog/company/{1}/'.format(PORT, company_id)).json()['company']
	print('View {0}'.format(company['name']))
	return render(request, 'catalog/view_company_id.html', {'company': company})


def add_company(request):
	print('Add company')
	return render(request, 'catalog/add_company.html')


def add_company_company(request, company_id=None):
	if company_id is None:
		company = {
			"company": {}
		}
	else:
		company = requests.get('http://localhost:{0}/catalog/company/{1}/'.format(PORT, company_id)).json()
	company['company']['name'] = request.POST['name']
	company['company']['place'] = request.POST['place']
	company['company']['date'] = request.POST['date']
	if company_id is None:
		requests.post('http://localhost:{0}/catalog/company/'.format(PORT), json=company)
	else:
		requests.put('http://localhost:{0}/catalog/company/{1}/'.format(PORT, company['company']['id']), json=company)
	return HttpResponseRedirect(reverse('catalog:view_company'))


def edit_company_id(request, company_id):
	company = requests.get('http://localhost:{0}/catalog/company/{1}/'.format(PORT, company_id)).json()['company']
	print('Edit {0}'.format(company['name']))
	return render(request, 'catalog/edit_company_id.html', {
		'company': company
	})


def edit_company_id_edit(request, company_id):
	return add_company_company(request, company_id)


def delete_company_id(request, company_id):
	company = requests.get('http://localhost:{0}/catalog/company/{1}/'.format(PORT, company_id)).json()['company']
	requests.delete('http://localhost:{0}/catalog/company/{1}/'.format(PORT, company_id))
	print('Delete {0}'.format(company['name']))
	return HttpResponseRedirect(reverse('catalog:view_company'))


def view_platform(request):
	print('Platform list')
	my_list = requests.get('http://localhost:{0}/catalog/platform/'.format(PORT)).json()
	paginator = Paginator(my_list['platform'], 5)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)
	return render(request, 'catalog/view_platform.html', {'contacts': contacts})


def view_platform_id(request, platform_id):
	platform = requests.get('http://localhost:{0}/catalog/platform/{1}/'.format(PORT, platform_id)).json()['platform']
	company = requests.get('http://localhost:{0}/catalog/company/{1}/'.format(PORT, platform['company'])).json()['company']
	print('View {0}'.format(platform['name']))
	return render(request, 'catalog/view_platform_id.html', {
		'platform': platform,
		'company': company
	})


def add_platform(request):
	print('Add platform')
	company = requests.get('http://localhost:{0}/catalog/company/'.format(PORT)).json()['company']
	return render(request, 'catalog/add_platform.html',  {
		'company': company
	})


def add_platform_platform(request, platform_id=None):
	if platform_id is None:
		platform = {
			"platform": {}
		}
	else:
		platform = requests.get('http://localhost:{0}/catalog/platform/{1}/'.format(PORT, platform_id)).json()
	platform['platform']['name'] = request.POST['name']
	platform['platform']['date'] = request.POST['date']
	platform['platform']['company'] = int(request.POST['company'])
	if platform_id is None:
		requests.post('http://localhost:{0}/catalog/platform/'.format(PORT), json=platform)
	else:
		requests.put('http://localhost:{0}/catalog/platform/{1}/'.format(PORT, platform['platform']['id']), json=platform)
	return HttpResponseRedirect(reverse('catalog:view_platform'))


def edit_platform_id(request, platform_id):
	platform = requests.get('http://localhost:{0}/catalog/platform/{1}/'.format(PORT, platform_id)).json()['platform']
	print('Edit {0}'.format(platform['name']))
	company = requests.get('http://localhost:{0}/catalog/company/'.format(PORT)).json()['company']
	return render(request, 'catalog/edit_platform_id.html', {
		'platform': platform,
		'company': company,
	})


def edit_platform_id_edit(request, platform_id):
	return add_platform_platform(request, platform_id)


def delete_platform_id(request, platform_id):
	platform = requests.get('http://localhost:{0}/catalog/platform/{1}/'.format(PORT, platform_id)).json()['platform']
	requests.delete('http://localhost:{0}/catalog/platform/{1}/'.format(PORT, platform_id))
	print('Delete {0}'.format(platform['name']))
	return HttpResponseRedirect(reverse('catalog:view_platform'))


def view_engine(request):
	print('Engine list')
	my_list = requests.get('http://localhost:{0}/catalog/engine/'.format(PORT)).json()
	paginator = Paginator(my_list['engine'], 5)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)
	return render(request, 'catalog/view_engine.html', {'contacts': contacts})


def view_engine_id(request, engine_id):
	engine = requests.get('http://localhost:{0}/catalog/engine/{1}/'.format(PORT, engine_id)).json()['engine']
	company = requests.get('http://localhost:{0}/catalog/company/{1}/'.format(PORT, engine['company'])).json()['company']
	print('View {0}'.format(engine['name']))
	return render(request, 'catalog/view_engine_id.html', {
		'engine': engine,
		'company': company
	})


def add_engine(request):
	print('Add engine')
	company = requests.get('http://localhost:{0}/catalog/company/'.format(PORT)).json()['company']
	return render(request, 'catalog/add_engine.html', {'company': company})


def add_engine_engine(request, engine_id=None):
	if engine_id is None:
		engine = {
			"engine": {}
		}
	else:
		engine = requests.get('http://localhost:{0}/catalog/engine/{1}/'.format(PORT, engine_id)).json()
	engine['engine']['name'] = request.POST['name']
	engine['engine']['language'] = request.POST['language']
	engine['engine']['date'] = request.POST['date']
	engine['engine']['company'] = int(request.POST['company'])
	if engine_id is None:
		requests.post('http://localhost:{0}/catalog/engine/'.format(PORT), json=engine)
	else:
		requests.put('http://localhost:{0}/catalog/engine/{1}/'.format(PORT, engine['engine']['id']), json=engine)
	return HttpResponseRedirect(reverse('catalog:view_engine'))


def edit_engine_id(request, engine_id):
	engine = requests.get('http://localhost:{0}/catalog/engine/{1}/'.format(PORT, engine_id)).json()['engine']
	print('Edit {0}'.format(engine['name']))
	company = requests.get('http://localhost:{0}/catalog/company/'.format(PORT)).json()['company']
	return render(request, 'catalog/edit_engine_id.html', {
		'engine': engine,
		'company': company,
	})


def edit_engine_id_edit(request, engine_id):
	return add_engine_engine(request, engine_id)


def delete_engine_id(request, engine_id):
	engine = requests.get('http://localhost:{0}/catalog/engine/{1}/'.format(PORT, engine_id)).json()['engine']
	requests.delete('http://localhost:{0}/catalog/engine/{1}/'.format(PORT, engine_id))
	print('Delete {0}'.format(engine['name']))
	return HttpResponseRedirect(reverse('catalog:view_engine'))
