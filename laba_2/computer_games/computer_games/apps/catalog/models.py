from django.db import models


class ComputerGame(models.Model):
    name = models.CharField('название', max_length=50)
    genre = models.CharField('жанр', max_length=50)
    setting = models.CharField('сеттинг', max_length=50)
    date = models.DateField('дата создания')


class Platform(models.Model):
    name = models.CharField('название', max_length=50)
    date = models.DateField('дата создания')
    game = models.ManyToManyField(ComputerGame)


class Engine(models.Model):
    name = models.CharField('название', max_length=50)
    language = models.CharField('язык программирования', max_length=50)
    date = models.DateField('дата создания')
    game = models.ForeignKey(ComputerGame, on_delete=models.CASCADE, null=True, blank=True)


class Company(models.Model):
    name = models.CharField('название', max_length=50)
    place = models.CharField('место расположения', max_length=50)
    date = models.DateField('дата создания')
    game = models.ForeignKey(ComputerGame, on_delete=models.CASCADE, null=True, blank=True)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, null=True, blank=True)
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE, null=True, blank=True)
