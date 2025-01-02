from django.db import models

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    STATUS_CHOICES = [
        ('N', 'New'),
        ('O', 'On-going'),
        ('E', 'Ended'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    team = models.ManyToManyField('Employee', related_name='projects')
    team_lead = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='led_projects')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    salary = models.FloatField()
    designation = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

