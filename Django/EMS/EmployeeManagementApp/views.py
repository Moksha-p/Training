from django.shortcuts import render
from EmployeeManagementApp.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from EmployeeManagementApp.serializers import *
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Sum, Max
from django.utils import timezone


# Create your views here.
class EmployeeView(APIView):
    def get(self, request):
        """Fetch all employee data."""
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a new employee."""
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailView(APIView):
    def get(self, request, pk):
        """Get employee data by ID."""
        employee = get_object_or_404(Employee, id=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk):
        """Update employee data by ID."""
        employee = get_object_or_404(Employee, id=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete an employee by ID."""
        employee = get_object_or_404(Employee, id=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeeDepartmentView(APIView):
    def get(self, request, pk):
        """Get department details by employee ID."""
        employee = get_object_or_404(Employee, id=pk)
        department = get_object_or_404(Department, id=employee.department_id)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)
    
class DepartmentView(APIView):
    # POST /departments/ to create a department
        def post(self, request):
            serializer = DepartmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET /departments/ to get all department data (without employee data)
        def get(self, request):
            departments = Department.objects.all()
            serializer = DepartmentSerializer(departments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

class DepartmentDetailView(APIView):
    # GET /departments/<id>/ to get department data along with all employees
    def get(self, request, id):
        try:
            department = Department.objects.get(id=id)
        except Department.DoesNotExist:
            return Response({"error": "Department not found."}, status=status.HTTP_404_NOT_FOUND)

        department_data = DepartmentSerializer(department).data
        employees = Employee.objects.filter(department=department)
        employees_data = [{"id": emp.id, "name": emp.name, "salary": emp.salary, "designation": emp.designation} for emp in employees]
        department_data["employees"] = employees_data
        return Response(department_data, status=status.HTTP_200_OK)

    # PUT /departments/<id>/ to update department data
    def put(self, request, id):
        try:
            department = Department.objects.get(id=id)
        except Department.DoesNotExist:
            return Response({"error": "Department not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE /departments/<id>/ to delete a department (with validation to check if employees exist)
    def delete(self, request, id):
        try:
            department = Department.objects.get(id=id)
        except Department.DoesNotExist:
            return Response({"error": "Department not found."}, status=status.HTTP_404_NOT_FOUND)

        employees = Employee.objects.filter(department=department)
        if employees.exists():
            return Response({"error": "Cannot delete department as employees exist in it."}, status=status.HTTP_400_BAD_REQUEST)

        department.delete()
        return Response({"message": "Department deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
class ProjectCreateView(APIView):
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectListView(APIView):
    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class ProjectAddMemberView(APIView):
    def put(self, request, id):
        project = get_object_or_404(Project, id=id)
        employee_ids = request.data.get('employee_ids', [])
        employees = Employee.objects.filter(id__in=employee_ids)
        project.team.add(*employees)
        return Response({'message': 'Employees added to project successfully.'})


class ProjectDetailView(APIView):
    def get(self, request, id):
        project = get_object_or_404(Project, id=id)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)


class ProjectDeleteView(APIView):
    def delete(self, request, id):
        project = get_object_or_404(Project, id=id)
        if project.end_date > timezone.now().date():
            return Response({'error': 'Cannot delete project before its end date.'}, status=status.HTTP_400_BAD_REQUEST)
        project.delete()
        return Response({'message': 'Project deleted successfully.'})


class ProjectUpdateStatusView(APIView):
    def put(self, request, id):
        project = get_object_or_404(Project, id=id)
        status = request.data.get('status')
        if status not in dict(Project.STATUS_CHOICES):
            return Response({'error': 'Invalid status.'}, status=status.HTTP_400_BAD_REQUEST)
        project.status = status
        project.save()
        return Response({'message': 'Project status updated successfully.'})


class ProjectBudgetView(APIView):
    def get(self, request, id):
        project = get_object_or_404(Project, id=id)
        total_salary = sum([employee.salary for employee in project.team.all()])
        return Response({'total_budget': total_salary})


class HighestSalaryEmployeeView(APIView):
    def get(self, request):
        highest_salary = Employee.objects.aggregate(Max('salary'))['salary__max']
        employees = Employee.objects.filter(salary=highest_salary)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


class SecondHighestSalaryEmployeeView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        results = []
        for department in departments:
            employees = Employee.objects.filter(department=department).order_by('-salary')
            if len(employees) > 1:
                second_highest = employees[1]
                results.append({
                    "department": department.name,
                    "employee": {
                        "id": second_highest.id,
                        "name": second_highest.name,
                        "salary": second_highest.salary,
                    },
                })
        return Response(results if results else {"message": "No second-highest salaries found."})


class TotalSalaryByDepartmentView(APIView):
    def get(self, request):
        departments = Department.objects.annotate(total_salary=Sum('employee__salary'))
        data = [
            {
                "department": department.name,
                "total_salary": department.total_salary or 0,
            }
            for department in departments
        ]
        return Response(data)


class NewProjectsView(APIView):
    def get(self, request):
        new_projects = Project.objects.filter(status='N')
        serializer = ProjectSerializer(new_projects, many=True)
        return Response(serializer.data)


class OngoingProjectsView(APIView):
    def get(self, request):
        ongoing_projects = Project.objects.filter(status='O')
        serializer = ProjectSerializer(ongoing_projects, many=True)
        return Response(serializer.data)


class EndedProjectsView(APIView):
    def get(self, request):
        ended_projects = Project.objects.filter(status='E')
        serializer = ProjectSerializer(ended_projects, many=True)
        return Response(serializer.data)