"""Views module to handle requests about Journal Entries"""

from urllib import request
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from app_api.serializers import EntrySerializer, UpdateEntrySerializer
from app_api.models import Entry
from datetime import datetime

now = datetime.now()

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
        current_user = request.auth.user.id          
                
        entry = Entry.objects.create(
            datetime = now,
            subject = request.data["subject"],
            body = request.data["body"],
            is_public = request.data["is_public"],
            developer_id = request.data["developer"]
        )
        
        # entry.developer.set(request.data[current_user])
        entry.save()
        entry.techtag.set(request.data["techtag"])
        entry.moodtag.set(request.data["moodtag"])
        
        serializer = EntrySerializer(entry, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
         
    
    # Update/Edit an Entry
    def update(self, request, pk):
        entry = Entry.objects.get(pk=pk)
        entry.subject = request.data["subject"]
        entry.body = request.data["body"]
        entry.is_public = request.data["is_public"]
        entry.techtag.set(request.data["techtag"])
        entry.moodtag.set(request.data["moodtag"])
        entry.save()
        
        serializer = EntrySerializer(entry, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
    
    # Delete Entry based on primary key
    def destroy(self, request, pk):
        entry = Entry.objects.get(pk=pk)
        entry.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
