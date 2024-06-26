from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Employee, Project, Leave
from .forms import EmployeeForm, ProjectForm, LeaveForm

@login_required
def dashboard(request):
    return render(request, 'ems/dashboard.html')

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'ems/employee_list.html', {'employees': employees})

@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'ems/employee_detail.html', {'form': form})

@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'ems/project_list.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'ems/project_detail.html', {'form': form})

@login_required
def leave_list(request):
    leaves = Leave.objects.all()
    return render(request, 'ems/leave_list.html', {'leaves': leaves})

@login_required
def leave_apply(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.employee = request.user.employee
            leave.status = 'Pending'
            leave.save()
            return redirect('leave_list')
    else:
        form = LeaveForm()
    return render(request, 'ems/leave_apply.html', {'form': form})
