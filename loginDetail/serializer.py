from rest_framework import serializers
from .models import UserLogin,TechLogin,Requests

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = '__all__'
        
        
class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechLogin
        fields = '__all__'
        

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = '__all__'