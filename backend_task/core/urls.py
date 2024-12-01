from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeListCreateView.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view()),
    path('employees/<int:pk>/department/', views.EmployeeDepartmentView.as_view()),
    path('employees/highest-salary/', views.HighestSalaryView.as_view()),

    path('departments/', views.DepartmentListCreateView.as_view()),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view()),

    path('projects/', views.ProjectListCreateView.as_view()),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view()),
    path('projects/<int:pk>/update-status/', views.ProjectUpdateStatusView.as_view()),
]
