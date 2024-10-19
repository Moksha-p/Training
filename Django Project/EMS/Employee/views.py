from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Employee, Department, Project
from .serializers import EmployeeSerializer, DepartmentSerializer, ProjectSerializer

class EmployeeListCreateView(generics.ListCreateAPIView) :
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDepartmentView(generics.RetrieveAPIView) :
    queryset = Employee.objects.all()

    def get(self, request, *args, **kwargs) :
        employee = self.get_object()
        department = employee.department
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

class DepartmentListCreateView(generics.ListCreateAPIView) :
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ProjectListCreateView(generics.ListCreateAPIView) :
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
        