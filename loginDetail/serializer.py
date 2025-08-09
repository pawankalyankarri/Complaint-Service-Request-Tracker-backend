from rest_framework import serializers
from .models import UserLogin,TechLogin

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = '__all__'
        
        
class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechLogin
        fields = '__all__'