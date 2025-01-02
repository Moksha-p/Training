"""EMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from EmployeeManagementApp.views import *

urlpatterns = [
    # Employee endpoints
    path('employees/', EmployeeView.as_view(), name='employee_list_create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('employees/<int:pk>/department/', EmployeeDepartmentView.as_view(), name='employee_department'),

    path('departments/', DepartmentView.as_view(), name='department-list-create'),
    path('departments/<int:id>/', DepartmentDetailView.as_view(), name='department-detail'),

    path('projects/', ProjectCreateView.as_view(), name='create_project'),
    path('projects/view/', ProjectListView.as_view(), name='list_projects'),
    path('projects/<int:id>/add-member/', ProjectAddMemberView.as_view(), name='add_member_to_project'),
    path('projects/<int:id>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:id>/delete/', ProjectDeleteView.as_view(), name='delete_project'),
    path('projects/<int:id>/update-status/', ProjectUpdateStatusView.as_view(), name='update_project_status'),
    path('projects/<int:id>/budget/', ProjectBudgetView.as_view(), name='project_budget'),
    path('employees/highest-salary/', HighestSalaryEmployeeView.as_view(), name='highest_salary_employee'),
    path('employees/second-highest-salary/', SecondHighestSalaryEmployeeView.as_view(), name='second_highest_salary_employee'),
    path('departments/total-salary/', TotalSalaryByDepartmentView.as_view(), name='total_salary_by_department'),
    path('projects/new/', NewProjectsView.as_view(), name='new_projects'),
    path('projects/on-going/', OngoingProjectsView.as_view(), name='ongoing_projects'),
    path('projects/ended/', EndedProjectsView.as_view(), name='ended_projects'),
]