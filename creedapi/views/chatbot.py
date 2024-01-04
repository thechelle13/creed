from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from creedapi.models import ChatBot


class ChatBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatBot
        fields = ['label']
        
class ChatBotViewSet(viewsets.ViewSet):
    def list(self, request):
        chatBots = ChatBot.objects.all()
        serializer = ChatBotSerializer(chatBots, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            chatBot = ChatBot.objects.get(pk=pk)
            serializer = ChatBotSerializer(chatBot)
            return Response(serializer.data)
        except ChatBot.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
