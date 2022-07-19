"""View module for handling requests about tags"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rarerestapi.models import Tag

class TagView(ViewSet):
    """Rare Rest Tag View"""

    def retrieve(self,request, pk):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized tag
        """
        tag = Tag.objects.get(pk=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all tags

        Returns:
            Response -- JSON serialized list of tags
        """

        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations
        
        Response -- JSON serialized game instance
        """
        tag = Tag.objects.create(
            label=request.data["label"]
        )
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized tag instance
        """

        tag = Tag.objects.create(
            label=request.data["label"],
        )
        serializer = TagSerializer(tag)
        return Response(serializer.data)

class TagSerializer(serializers.ModelSerializer):
    """JSON serializer tags
    """
    class Meta:
        model = Tag
        fields = ('id', 'label')