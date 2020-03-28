from rest_framework import serializers

from .models import ComputerGame, Company, Platform, Engine

class ComputerGameSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    genre = serializers.CharField(max_length=50)
    setting = serializers.CharField(max_length=50)
    date = serializers.DateField()

    def create(self, validated_data):
            return ComputerGame.objects.create(**validated_data)