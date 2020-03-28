from django.db import models


class Company(models.Model):
    name = models.CharField('название', max_length=50)
    place = models.CharField('место расположения', max_length=50)
    date = models.DateField('дата создания')


class Engine(models.Model):
    name = models.CharField('название', max_length=50)
    language = models.CharField('язык программирования', max_length=50)
    date = models.DateField('дата создания')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)


class Platform(models.Model):
    name = models.CharField('название', max_length=50)
    date = models.DateField('дата создания')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)


class ComputerGame(models.Model):
    name = models.CharField('название', max_length=50)
    genre = models.CharField('жанр', max_length=50)
    setting = models.CharField('сеттинг', max_length=50)
    date = models.DateField('дата создания')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE, null=True, blank=True)
    platform = models.ManyToManyField(Platform)
