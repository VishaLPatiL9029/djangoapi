from django.contrib import admin
from django.urls import path, include
from api.views import CompanyViewset, EmployeeViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'companies', CompanyViewset)
router.register(r'employees', EmployeeViewset)

urlpatterns = [
    path('', include(router.urls))
]



#compnies/{company_id}/employees