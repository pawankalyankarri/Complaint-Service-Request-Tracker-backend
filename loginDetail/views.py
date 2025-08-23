from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_201_CREATED
from .serializer import UserSerializer,TechSerializer,RequestSerializer,DepartmentsSerializer,AccReqSerializer
from .models import UserLogin,TechLogin,Requests,Departments,AcceptedRequests
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
        
        
        
class RaiseRequests(APIView):
    def get(self,req):
        requests = Requests.objects.all()
        ser_obj = RequestSerializer(requests,many=True)
        return Response(ser_obj.data,status=HTTP_200_OK)
    
    def post(self,req):
        ser_obj = RequestSerializer(data = req.data)
        if ser_obj.is_valid():
            new_req = ser_obj.save()
            created_obj = RequestSerializer(new_req).data
            return Response(created_obj,status=HTTP_201_CREATED)
        else:
            return Response(ser_obj.errors,status=HTTP_400_BAD_REQUEST)
        
        
class GetDepartments(APIView):
    def get(self,req):
        depts = Departments.objects.all()
        ser_obj = DepartmentsSerializer(depts,many = True)
        return Response(ser_obj.data,status=HTTP_200_OK)
    
    def post(self,req):
        ser_obj = DepartmentsSerializer(data = req.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(ser_obj.errors,status=HTTP_400_BAD_REQUEST)
        
        
      
      
class AcceptingRequest(APIView):
    def get(self,req):
        acc_reqs = AcceptedRequests.objects.all()
        ser_obj = AccReqSerializer(acc_reqs,many=True)
        return Response(ser_obj.data,status=HTTP_200_OK)
    
    def post(self,req):
        ser_obj = AccReqSerializer(data = req.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(ser_obj.errors,status=HTTP_400_BAD_REQUEST)
        
        
        
class ModifyAcceptingRequest(APIView):
    def put(self,req,pk):
        req_obj = AcceptedRequests.objects.get(areq_id = pk)
        ser_obj = AccReqSerializer(data = req_obj)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(ser_obj.errors,status=HTTP_400_BAD_REQUEST)
            
    def get(self,req,pk):
        req_obj = AcceptedRequests.objects.get(areq_id = pk)
        ser_obj = AccReqSerializer(req_obj)
        return Response(ser_obj.data,status=HTTP_200_OK)
            