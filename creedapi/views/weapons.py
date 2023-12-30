from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from creedapi.models import Weapon


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ['label']
        
class WeaponViewSet(viewsets.ViewSet):
    def list(self, request):
        weapons = Weapon.objects.all()
        serializer = WeaponSerializer(weapons, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            weapon = Weapon.objects.get(pk=pk)
            serializer = WeaponSerializer(weapon)
            return Response(serializer.data)
        except Weapon.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)