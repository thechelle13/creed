from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from creedapi.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['label']
        
class GameViewSet(viewsets.ViewSet):
    def list(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)