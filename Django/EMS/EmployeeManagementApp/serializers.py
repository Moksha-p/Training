from rest_framework import serializers
from .models import Department, Employee, Project

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())

    class Meta:
        model = Employee
        fields = ['id', 'name', 'salary', 'designation', 'department', 'address']

class ProjectSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), many=True)
    team_lead = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())  
    status = serializers.ChoiceField(choices=Project.STATUS_CHOICES)  

    class Meta:
        model = Project
        fields = ['id', 'name', 'team', 'team_lead', 'status', 'start_date', 'end_date']
