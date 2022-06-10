"""Views module to handle request about Journal Entries"""

from urllib import request
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from app_api.serializers import EntrySerializer, UpdateEntrySerializer
from app_api.models import Entry, techtag



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



    # Create new Entry
    def create(self, request):
        entry = Entry.objects.create(
            subject = request.data["subject"],
            body = request.data["body"],
            is_public = request.data["is_public"],
            techtag = request.data["techtag"],
            moodtag = request.data["moodtag"]            
        )
        serializer = EntrySerializer(entry)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
    # Update/Edit a Entry
    def update(self, request, pk):
        entry = Entry.objects.get(pk=pk)
        serializer = EntrySerializer(entry, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
    
    # Delete Entry based on primary key
    def destroy(self, request, pk):
        entry = Entry.objects.get(pk=pk)
        entry.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
