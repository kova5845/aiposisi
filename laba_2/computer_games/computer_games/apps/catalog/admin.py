from django.contrib import admin
from .models import ComputerGame, Company, Platform, Engine


admin.site.register(ComputerGame)
admin.site.register(Company)
admin.site.register(Platform)
admin.site.register(Engine)
