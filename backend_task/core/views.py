from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Max, Sum
from .models import Department, Employee, Project
from .serializers import DepartmentSerializer, EmployeeSerializer, ProjectSerializer


# Employee APIs
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDepartmentView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = DepartmentSerializer

    def get_object(self):
        employee = super().get_object()
        return employee.department


class HighestSalaryView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        max_salary = Employee.objects.aggregate(Max('salary'))['salary__max']
        return Employee.objects.filter(salary=max_salary)


# Department APIs
class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def perform_destroy(self, instance):
        if instance.employee_set.exists():
            raise serializers.ValidationError("Cannot delete department with employees.")
        instance.delete()


# Project APIs
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_destroy(self, instance):
        if instance.end_date > timezone.now().date():
            raise serializers.ValidationError("Cannot delete a project that hasn't ended.")
        instance.delete()


class ProjectUpdateStatusView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def update(self, request, *args, **kwargs):
        project = self.get_object()
        project.status = request.data.get('status')
        project.save()
        return Response(ProjectSerializer(project).data)
