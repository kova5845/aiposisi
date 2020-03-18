from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import ComputerGame, Company, Platform, Engine
from django.urls import reverse
from datetime import datetime


def index(request):
	return render(request, 'base.html')


def view(request):
	game_list = ComputerGame.objects.all()
	return render(request, 'catalog/list.html', {'game_list': game_list})


def edit(request):
	return HttpResponse('Edit')


def add(request):
	return HttpResponse('Add')


def view_game(request, game_id):
	try:
		game = ComputerGame.objects.get(id=game_id)
	except:
		raise Http404('Игра не найдена')

	return render(request, 'catalog/view_game.html', {'game': game})


def edit_game(request, game_id):
	try:
		game = ComputerGame.objects.get(id=game_id)
	except:
		raise Http404('Игра не найдена')

	return render(request, 'catalog/edit_game.html', {'game': game, 'game_date': game.date.strftime('%Y-%m-%d')})


def edit_game_id(request, game_id):
	try:
		game = ComputerGame.objects.get(id=game_id)
		game.name = request.POST['name']
		game.genre = request.POST['genre']
		game.setting = request.POST['setting']
		game.date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
		game.save()
	except:
		raise Http404('Игра не найдена')

	return HttpResponseRedirect(reverse('catalog:edit_game', args=(game.id,)))
