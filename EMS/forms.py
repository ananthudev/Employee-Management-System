from django import forms
from django.contrib.auth.models import User
from .models import Employee, Project, Leave

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['designation', 'department']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'team_members']

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['start_date', 'end_date', 'reason']
