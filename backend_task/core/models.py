from django.db import models


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('ON-GOING', 'On-Going'),
        ('ENDED', 'Ended'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    team_lead = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, related_name='lead_projects')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='NEW')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    salary = models.FloatField()
    designation = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    address = models.CharField(max_length=255)
    projects = models.ManyToManyField(Project, related_name='team_members', blank=True)

    def __str__(self):
        return self.name
