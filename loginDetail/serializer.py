from rest_framework import serializers
from .models import UserLogin,TechLogin,Requests,Departments,AcceptedRequests

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
        

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'
        

class AccReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcceptedRequests
        fields = '__all__'