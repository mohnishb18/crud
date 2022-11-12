from django.contrib.auth.context_processors import auth
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import *
from .filters import *
from rest_framework import viewsets
from .serializer import *
from .models import *
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
#decorators
from rest_framework.decorators import api_view
from rest_framework.response import Response
#Authentication and permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny



# Create your views here.
import json
def webpage(request):
    my_dict={'insert_me':'hello i am from views.py :'}
    return render(request,'webpage.html',context=my_dict)

def index(request):
    return HttpResponse('welcome to homepage')

def EmpEntry(request):
    form=EmployeeForm
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/data')
    return render(request,'Empform.html',{'form':form})


def EmpData(request):
    data=Employee.objects.all()
    return render(request,'EmpData.html',{'data':data})


def UpdateEmp(request,id):
    name=Employee.objects.get(id=id)
    form=EmployeeForm(instance=name)
    if request.method=='POST':
        form=EmployeeForm(request.POST or None,instance=name)
        if form.is_valid():
            form.save()
    return render(request,'updateform.html',{'form':form})


def Empdelete(request,id):
    name=Employee.objects.get(id=id)
    name.delete()
    return redirect('/data')

def SearchEmp(request):
    search=Employee.objects.all()
    filters=FilterEmployeeInfo(request.GET,queryset=search)
    return render(request,'search.html',{'filters':filters})

class EmployeeViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer

def home(request):
    url = 'http://freegeoip.net/json/'
    response=requests.get(url)
    geodata=response.json()
    return render(request,'home.html',{'ip':geodata['id'],'country':geodata['country']})


class GenerateCredential(APIView):
    def get(self, request, format=None):
        results=self.request.query_params.get('type')
        response={}
        r=request.get('https://randomuser.me/api/?result=40', auth('user','pass'))
        r_status=r.status_code

        if r_status==200:
            data=json.loads(r.json)

            for c in data:
                credential=Credential(user=self.request.user,value=c)
                credential.save()
            response['status']=200
            response['message']='success'
            response['credential']=data
        else:
            response['status']=r.status_code
            response['message']='error'
            response['credentiall']={}
        return Response(response)


@api_view(['POST'])
def index1(request):
    return Response({'status':200,'message':'hello world'})

@api_view(['GET'])
def home1(request):
    emp_obj =Employee.objects.all()
    serializer=Employeeserializer(emp_obj,many=True)
    return Response({'status':200,'payload':serializer.data})

@api_view(['POST'])
def post_emp(request):
    data=request.data
    serializer=Employeeserializer(data=request.data)

    # if request.data['esal'] < 10000:
    #     return Response({'status':403,'message':'Salary must be greater than 10000'})
    #
    # if request.data['ename'].isdigit():
    #     return Response({'status':403,'error':'name cannot be in numeric'})


    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status':403,'message':'your data is not submitted'})
    serializer.save()

    return Response({'status':200,'message':'your data is submitted'})


@api_view(['PUT'])
def update_employee(request,eid):
    try:
        emp_obj=Employee.objects.get(eid=eid)
        serializer=Employeeserializer(emp_obj,data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,'errors':serializer.errors,'message':'your data is not submitted'})

        serializer.save()
        return Response({'status': 200,'errors':serializer.errors ,'message': 'your data is submitted'})

    except Exception as e:
        return Response({'status':403,'error':'invalid id'})
