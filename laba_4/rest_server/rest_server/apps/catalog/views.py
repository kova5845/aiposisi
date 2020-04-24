from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from .models import ComputerGame, Company, Platform, Engine
from .serializers import ComputerGameSerializer, CompanySerializer, PlatformSerializer, EngineSerializer


class ComputerGameView(APIView):

    def get(self, request):
        game = ComputerGame.objects.all()
        serializer = ComputerGameSerializer(game, many=True)
        return Response({"game": serializer.data})

    def post(self, request):
        game = request.data.get('game')
        serializer = ComputerGameSerializer(data=game)
        if serializer.is_valid(raise_exception=True):
            game_saved = serializer.save()
        return Response({"success": "Game '{}' created successfully".format(game_saved.name)})


class ComputerGameIdView(APIView):

    def get(self, request, pk):
        game = get_object_or_404(ComputerGame.objects.all(), pk=pk)
        serializer = ComputerGameSerializer(game)
        return Response({"game": serializer.data})

    def put(self, request, pk):
        saved_game = get_object_or_404(ComputerGame.objects.all(), pk=pk)
        data = request.data.get('game')
        serializer = ComputerGameSerializer(instance=saved_game, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            game_saved = serializer.save()
        return Response({
            "success": "Game '{}' updated successfully".format(game_saved.name)
        })

    def delete(self, request, pk):
        game = get_object_or_404(ComputerGame.objects.all(), pk=pk)
        game.delete()
        return Response({
            "message": "Game with id `{}` has been deleted.".format(pk)
        }, status=204)


class CompanyView(APIView):

    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response({"company": serializer.data})

    def post(self, request):
        company = request.data.get('company')
        serializer = CompanySerializer(data=company)
        if serializer.is_valid(raise_exception=True):
            company_saved = serializer.save()
        return Response({"success": "Company '{}' created successfully".format(company_saved.name)})


class CompanyIdView(APIView):

    def get(self, request, pk):
        company = get_object_or_404(Company.objects.all(), pk=pk)
        serializer = CompanySerializer(company)
        return Response({"company": serializer.data})

    def put(self, request, pk):
        saved_company = get_object_or_404(Company.objects.all(), pk=pk)
        data = request.data.get('company')
        serializer = CompanySerializer(instance=saved_company, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            company_saved = serializer.save()
        return Response({
            "success": "Company '{}' updated successfully".format(company_saved.name)
        })

    def delete(self, request, pk):
        company = get_object_or_404(Company.objects.all(), pk=pk)
        company.delete()
        return Response({
            "message": "Company with id `{}` has been deleted.".format(pk)
        }, status=204)


class PlatformView(APIView):

    def get(self, request):
        platform = Platform.objects.all()
        serializer = PlatformSerializer(platform, many=True)
        return Response({"platform": serializer.data})

    def post(self, request):
        platform = request.data.get('platform')
        serializer = PlatformSerializer(data=platform)
        if serializer.is_valid(raise_exception=True):
            platform_saved = serializer.save()
        return Response({"success": "Platform '{}' created successfully".format(platform_saved.name)})


class PlatformIdView(APIView):

    def get(self, request, pk):
        platform = get_object_or_404(Platform.objects.all(), pk=pk)
        serializer = PlatformSerializer(platform)
        return Response({"platform": serializer.data})

    def put(self, request, pk):
        saved_platform = get_object_or_404(Platform.objects.all(), pk=pk)
        data = request.data.get('platform')
        serializer = PlatformSerializer(instance=saved_platform, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            platform_saved = serializer.save()
        return Response({
            "success": "Platform '{}' updated successfully".format(platform_saved.name)
        })

    def delete(self, request, pk):
        platform = get_object_or_404(Platform.objects.all(), pk=pk)
        platform.delete()
        return Response({
            "message": "Platform with id `{}` has been deleted.".format(pk)
        }, status=204)


class EngineView(APIView):

    def get(self, request):
        engine = Engine.objects.all()
        serializer = EngineSerializer(engine, many=True)
        return Response({"engine": serializer.data})

    def post(self, request):
        engine = request.data.get('engine')
        serializer = EngineSerializer(data=engine)
        if serializer.is_valid(raise_exception=True):
            engine_saved = serializer.save()
        return Response({"success": "Engine '{}' created successfully".format(engine_saved.name)})


class EngineIdView(APIView):

    def get(self, request, pk):
        engine = get_object_or_404(Engine.objects.all(), pk=pk)
        serializer = EngineSerializer(engine)
        return Response({"engine": serializer.data})

    def put(self, request, pk):
        saved_engine = get_object_or_404(Engine.objects.all(), pk=pk)
        data = request.data.get('engine')
        serializer = EngineSerializer(instance=saved_engine, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            engine_saved = serializer.save()
        return Response({
            "success": "Engine '{}' updated successfully".format(engine_saved.name)
        })

    def delete(self, request, pk):
        engine = get_object_or_404(Engine.objects.all(), pk=pk)
        engine.delete()
        return Response({
            "message": "Engine with id `{}` has been deleted.".format(pk)
        }, status=204)
