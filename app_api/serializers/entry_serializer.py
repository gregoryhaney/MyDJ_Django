from rest_framework import serializers
from app_api.models import Entry



class EntrySerializer(serializers.ModelSerializer):
        
    """JSON serializer for entry
    """
    class Meta:
        model = Entry
        fields = ('id', 'datetime', 'subject', 'body',
                  'is_public', 'techtag', 'moodtag', 'developer')
        depth = 1


class UpdateEntrySerializer(serializers.ModelSerializer):
        
    """JSON serializer for entry
    """
    class Meta:
        model = Entry
        fields = ('id', 'subject', 'body',
                  'is_public', 'techtag', 'moodtag')
       