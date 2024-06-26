from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    employees = models.ManyToManyField(Employee, related_name='projects')

    def __str__(self):
        return self.name

class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=(('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')))

    def __str__(self):
        return f'{self.employee.user.username} - {self.status}'
