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


#projects table
class Project(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('inprogress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    name = models.CharField(max_length=200)
    employees = models.ManyToManyField(Employee)
    start_date = models.DateField(null=True, blank=False)
    end_date = models.DateField(null=True, blank=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, null=True, blank=False)
    task_description = models.TextField(null=True, blank=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True, blank=False)

    def __str__(self):
        return self.name

#projects table end

# leaves model start
class Leave(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('casual', 'Casual'),
        ('sick', 'Sick'),
        ('personal', 'Personal'),
        ('vacation', 'Vacation'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    apply_date = models.DateField(auto_now_add=True, null=True)
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES, null=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', null=True)

    def __str__(self):
        return f'{self.employee.name} - {self.leave_type}'

    class Meta:
        verbose_name_plural = "Leaves"



# leaves model end

