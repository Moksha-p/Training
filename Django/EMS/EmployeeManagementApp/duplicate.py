from django.shortcuts import render
from EmployeeManagementApp.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from EmployeeManagementApp.serializers import *
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Sum


# Create your views here.
class EmployeeDetailView(APIView):
    def get(self, request, pk):
        try:
            employee = get_object_or_404(Employee, id=pk)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class EmployeeView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        employee = get_object_or_404(Employee, id=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        employee = get_object_or_404(Employee, id=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get_department_details_using_employee_id(self, request, pk):
        employee = get_object_or_404(Employee, id=pk)
        department = get_object_or_404(Department, id=employee.department_id)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

class DepartmentView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        department = get_object_or_404(Department, id=pk)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk):
        try:
            department = get_object_or_404(Department, id=pk)
            employees = Employee.objects.filter(department=department)
            department_serializer = DepartmentSerializer(department)
            employee_serializer = EmployeeSerializer(employees, many=True)
            
            department_data = department_serializer.data
            department_data['employees'] = employee_serializer.data
            return Response(department_data)
        except Department.DoesNotExist:
            return Response({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        department = get_object_or_404(Department, id=pk)
        if department.employee_set.exists():
            return Response({"error": "Department cannot be deleted because it has employees."},
                            status=status.HTTP_400_BAD_REQUEST)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        project = get_object_or_404(Project, id=pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk):
        try:
            project = get_object_or_404(Project, id=pk)
            serializer = ProjectSerializer(project)
            return Response(serializer.data)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        project = get_object_or_404(Project, id=pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        project = get_object_or_404(Project, id=pk)
        status_value = request.data.get('status')
        if status_value in ['N', 'O', 'E']:
            project.status = status_value
            project.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk):
        project = get_object_or_404(Project, id=pk)
        total_salary = project.team.aggregate(Sum('salary'))['salary__sum']
        return Response({"budget": total_salary}, status=status.HTTP_200_OK)

    @staticmethod
    def highest_salary(self, request):
        highest_paid_employee = Employee.objects.order_by('-salary').first()
        if highest_paid_employee:
            serializer = EmployeeSerializer(highest_paid_employee)
            return Response(serializer.data)
        return Response({"message": "No employees found"}, status=status.HTTP_404_NOT_FOUND)
    
    @staticmethod
    def second_highest_salary(request):
        departments = Department.objects.all()
        result = []
        for department in departments:
            employees = department.employee_set.order_by('-salary')
            if len(employees) > 1:
                second_highest = employees[1]
                result.append({
                    'department': department.name,
                    'second_highest_salary_employee': EmployeeSerializer(second_highest).data
                })
        return Response(result, status=status.HTTP_200_OK)

    @staticmethod
    def total_salary_by_department(request):
        departments = Department.objects.all()
        result = []
        for department in departments:
            total_salary = department.employee_set.aggregate(Sum('salary'))['salary__sum']
            result.append({
                'department': department.name,
                'total_salary': total_salary
            })
        return Response(result, status=status.HTTP_200_OK)

    @staticmethod
    def new_projects(request):
        projects = Project.objects.filter(status='N')
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @staticmethod
    def ongoing_projects(request):
        projects = Project.objects.filter(status='O')
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @staticmethod
    def ended_projects(request):
        projects = Project.objects.filter(status='E')
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)