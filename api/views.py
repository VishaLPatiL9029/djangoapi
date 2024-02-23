from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.response import Response
# Create your views here.
class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    #companies/{company_id}/employees
    @action(detail = True, methods = ['get'])
    def employees(self, request, pk = None):
        try:            
            company = Company.objects.get(pk = pk)
            emps = Employee.objects.filter(company = company)
            emps_serializer = EmployeeSerializer(emps, many=True, context = {'request' : request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'company might not exists !! Error'
            })
            
class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer