"""Views module to handle request about Techtags"""

from urllib import request
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.serializers import TechtagSerializer
from app_api.models import Techtag



class TechtagView(ViewSet):
    """ViewSet for TechtagView - get the collection of techtags from DB
        Returns:
            Response -- JSON serialized list of all techtags    
    """
    
    # Get all Techtags
    def list(self, request):
        techtag = Techtag.objects.all()          # ORM method "all"
        serializer = TechtagSerializer(techtag, many=True)
        return Response(serializer.data)
    
    
    # Get individual Techtag based on primary key
    def retrieve(self, request, pk):
        try:
            techtag = Techtag.objects.get(pk=pk)
            serializer = TechtagSerializer(techtag)
            return Response(serializer.data)      
        except Techtag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)




    #   SERIALIZERS MOVED TO THEIR OWN DIR

