from rest_framework import serializers
from app_api.models import Techtag

class TechtagSerializer(serializers.ModelSerializer):
        
    """JSON serializer for techtag
    """
    class Meta:
        model = Techtag
        fields = ('id', 'tech_title')