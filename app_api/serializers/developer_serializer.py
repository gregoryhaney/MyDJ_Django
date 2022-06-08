from rest_framework import serializers
from app_api.models import Developer



class DeveloperSerializer(serializers.ModelSerializer):
        
    """JSON serializer for entry
    """
    class Meta:
        model = Developer
        fields = ('id', 'first_name', 'last_name',
                  'nickname', 'email', 'user')
        
    