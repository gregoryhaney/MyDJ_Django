"""Views module to handle requests about Developers"""

from urllib import request
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models.developer import Developer
from app_api.serializers import DeveloperSerializer
from app_api.models import Entry


class DeveloperView(ViewSet):
    """ViewSet for DeveloperView - get the collection of 
            Developers from DB
        Returns:
            Response -- JSON serialized list of all Developers    
    """
    
    # Get all Developers
    def list(self, request):
        developer = Developer.objects.all()          # ORM method "all"
        serializer = DeveloperSerializer(developer, many=True)
        return Response(serializer.data)
    
    
    # Get an individual Developer based on primary key
    def retrieve(self, request, pk):
        try:
            developer = Developer.objects.get(pk=pk)
            serializer = DeveloperSerializer(developer)
            return Response(serializer.data)      
        except Developer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

