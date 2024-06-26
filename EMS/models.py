from django.db import models
from django.contrib.auth.models import User


#employee start
from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    s1_no = models.CharField(max_length=20, null=True, blank=False)
    name = models.CharField(max_length=100, null=True, blank=False)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=False)
    role = models.CharField(max_length=100, null=True, blank=False)
    department = models.CharField(max_length=100, null=True, blank=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            # Generate s1_no when creating a new instance
            self.s1_no = f'S1-{Employee.objects.count() + 1:04}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name  # Adjust this to return an appropriate representation

    class Meta:
        verbose_name_plural = "Employees"  # Optionally adjust plural name

#employee end

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    team_members = models.ManyToManyField(Employee, related_name='projects')

    def __str__(self):
        return self.name

class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=50, choices=(('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')))

    def __str__(self):
        return f'{self.employee.user.username} - {self.status}'
