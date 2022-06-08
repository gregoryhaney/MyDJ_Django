"""Views module to handle request about Journal Entries"""

from urllib import request
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.serializers import EntrySerializer
from app_api.models import Entry



class EntryView(ViewSet):
    """ViewSet for EntryView - get the collection of 
            Journal Entries from DB
        Returns:
            Response -- JSON serialized list of all Journal Entries    
    """
    
    # Get all Entries
    def list(self, request):
        entry = Entry.objects.all()          # ORM method "all"
        serializer = EntrySerializer(entry, many=True)
        return Response(serializer.data)
    
    
    # Get an individual Entry based on primary key
    def retrieve(self, request, pk):
        try:
            entry = Entry.objects.get(pk=pk)
            serializer = EntrySerializer(entry)
            return Response(serializer.data)      
        except Entry.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)




    #   SERIALIZERS MOVED TO THEIR OWN DIR


    