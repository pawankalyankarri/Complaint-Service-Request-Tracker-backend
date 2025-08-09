from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_201_CREATED
from .serializer import UserSerializer,TechSerializer
from .models import UserLogin,TechLogin
# Create your views here.

class LoginUser(APIView):
    def get(self,req):
        users = UserLogin.objects.all()
        ser_obj = UserSerializer(users,many=True)
        return Response(ser_obj.data,status=HTTP_200_OK)
    
    def post(self,req):
        ser_obj = UserSerializer(data = req.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(ser_obj.errors,status=HTTP_400_BAD_REQUEST)
        

class LoginTech(APIView):
    def get(self,req):
        techs = TechLogin.objects.all()
        seri_obj = TechSerializer(techs,many=True)
        return Response(seri_obj.data,status=HTTP_200_OK)
    
    def post(self,req):
        seri_obj = TechSerializer(data = req.data)
        if seri_obj.is_valid():
            seri_obj.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(seri_obj.errors,status=HTTP_400_BAD_REQUEST)