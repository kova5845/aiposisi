from rest_framework import serializers

from .models import ComputerGame, Company, Platform, Engine


class ComputerGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerGame
        fields = ('id', 'name', 'genre', 'setting', 'date', 'company', 'engine', 'platform')

    def create(self, validated_data):
        instance = ComputerGame()
        instance.name = validated_data.get('name')
        instance.genre = validated_data.get('genre')
        instance.setting = validated_data.get('setting')
        instance.date = validated_data.get('date')
        instance.save()
        instance.company = validated_data.get('company')
        instance.engine = validated_data.get('engine')
        instance.platform.set(validated_data.get('platform'))
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.setting = validated_data.get('setting', instance.setting)
        instance.date = validated_data.get('date', instance.date)
        instance.company = validated_data.get('company', instance.company)
        instance.engine = validated_data.get('engine', instance.engine)
        instance.platform.set(validated_data.get('platform', instance.platform))
        instance.save()
        return instance


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'place', 'date')

    def create(self, validated_data):
        instance = Company()
        instance.name = validated_data.get('name')
        instance.place = validated_data.get('place')
        instance.date = validated_data.get('date')
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.place = validated_data.get('place', instance.place)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ('id', 'name', 'date', 'company')

    def create(self, validated_data):
        instance = Platform()
        instance.name = validated_data.get('name')
        instance.date = validated_data.get('date')
        instance.save()
        instance.company = validated_data.get('company')
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.date = validated_data.get('date', instance.date)
        instance.company = validated_data.get('company', instance.company)
        instance.save()
        return instance


class EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = ('id', 'name', 'language', 'date', 'company')

    def create(self, validated_data):
        instance = Engine()
        instance.name = validated_data.get('name')
        instance.language = validated_data.get('language')
        instance.date = validated_data.get('date')
        instance.save()
        instance.company = validated_data.get('company')
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.language = validated_data.get('language', instance.language)
        instance.date = validated_data.get('date', instance.date)
        instance.company = validated_data.get('company', instance.company)
        instance.save()
        return instance
