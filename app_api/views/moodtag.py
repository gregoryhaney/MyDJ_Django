"""Views module to handle request about Moodtags"""

from urllib import request
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.serializers import MoodtagSerializer
from app_api.models import Moodtag



class MoodtagView(ViewSet):
    """ViewSet for MoodtagView - get the collection of moodtags from DB
        Returns:
            Response -- JSON serialized list of all moodtags    
    """
    
    # Get all Moodtags
    def list(self, request):
        moodtag = Moodtag.objects.all()          # ORM method "all"
        serializer = MoodtagSerializer(moodtag, many=True)
        return Response(serializer.data)
    
    
    # Get individual Moodtag based on primary key
    def retrieve(self, request, pk):
        try:
            moodtag = Moodtag.objects.get(pk=pk)
            serializer = MoodtagSerializer(moodtag)
            return Response(serializer.data)      
        except Moodtag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)




    #   SERIALIZERS MOVED TO THEIR OWN DIR


