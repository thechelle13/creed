from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from creedapi.models import Character
from creedapi.models import CreedUser


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ["id",
                  "game",
                  "level",
                  "name",
                #   "image_url",
                  "creed_user"
                  ]


class CharacterViewSet(viewsets.ViewSet):
    def list(self, request):
        characters = Character.objects.all()
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            character = Character.objects.get(pk=pk)
            serializer = CharacterSerializer(character)
            return Response(serializer.data)
        except Character.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        # Get the data from the client's JSON payload
        creed_user = CreedUser.objects.get(user=request.auth.user)
        name = request.data.get("name")
        game = request.data.get("game")
        # image_url = request.data.get("image_url")
        level = request.data.get("level")
              

        # Create a comment database row first, so you have a
        # primary key to work with
        character = Character.objects.create(
           
            game=game,
            level=level,
            name=name,
            # image_url=image_url,
            creed_user=creed_user,
            
            
        )

        serializer = CharacterSerializer(character, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        try:
            character = Character.objects.get(pk=pk)

            # Is the authenticated user allowed to edit this tag?
            self.check_object_permissions(request, character)

            serializer = CharacterSerializer(data=request.data)
            if serializer.is_valid():
                character.game = serializer.validated_data["game"]
                character.level = serializer.validated_data["level"]
                character.image_url = serializer.validated_data["image_url"]
                character.name = serializer.validated_data["name"]
                # tag.created_on = serializer.validated_data["created_on"]
                character.save()

                serializer = CharacterSerializer(character, context={"request": request})
                return Response(None, status.HTTP_204_NO_CONTENT)

            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        except character.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            character = Character.objects.get(pk=pk)
            self.check_object_permissions(request, character)
            character.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except character.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)