from django.urls import path
from .views import (
    EmployeeListCreateView, EmployeeDetailView, EmployeeDepartmentView,
    DepartmentListCreateView, DepartmentDetailView,
    ProjectListCreateView, ProjectDetailView
)    

urlpatterns = [
    path('Employee/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('Employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('Employee/<int:pk>/department/', EmployeeDepartmentView.as_view(), name='employee-department'),

    path('departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),

    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]