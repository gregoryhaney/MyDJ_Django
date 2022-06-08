from rest_framework import serializers
from app_api.models import Moodtag




class MoodtagSerializer(serializers.ModelSerializer):
        
    """JSON serializer for moodtag
    """
    class Meta:
        model = Moodtag
        fields = ('id', 'tag_title')
        