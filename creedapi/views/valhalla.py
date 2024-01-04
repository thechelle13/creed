from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from creedapi.models import Valhalla


class ValhallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valhalla
        fields = ['location']
        
class ValhallaViewSet(viewsets.ViewSet):
    def list(self, request):
        valhallas = Valhalla.objects.all()
        serializer = ValhallaSerializer(valhallas, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            valhalla = Valhalla.objects.get(pk=pk)
            serializer = ValhallaSerializer(valhalla)
            return Response(serializer.data)
        except Valhalla.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)