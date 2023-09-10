from rest_framework import serializers
from .models import *

class GetSubscriberSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
    
class AddSubscriberSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    