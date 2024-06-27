from django import forms
from django.contrib.auth.models import User
from .models import Employee, Project, Leave


# employee form start
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'phone', 'role', 'department']  
        
# employee form end
class ProjectForm(forms.ModelForm):
    employees = forms.ModelMultipleChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Select Employees (Only 5 maximum employees allowed)"
    )

    class Meta:
        model = Project
        fields = ['name', 'employees', 'start_date', 'end_date', 'priority', 'task_description', 'status']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_employees(self):
        employees = self.cleaned_data.get('employees')
        if employees.count() > 5:
            raise forms.ValidationError("You can select a maximum of 5 employees.")
        return employees

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['start_date', 'end_date', 'reason']
