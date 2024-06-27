from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from .models import Employee, Project, Leave
from .forms import EmployeeForm, ProjectForm, LeaveForm
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
# dashboard 
@login_required
def dashboard(request):
    return render(request, 'ems/dashboard.html')

# dashboard

# employee operations start 
@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'ems/employee_list.html', {'employees': employees})

@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.user = request.user
            employee.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'ems/employee_form.html', {'form': form})

@login_required
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'ems/employee_form.html', {'form': form})

@login_required
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'ems/employee_confirm_delete.html', {'employee': employee})

@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'ems/employee_detail.html', {'employee': employee})



# employee operations ends here

#logout 
def logout(request):
    auth_logout(request)
    return redirect('login')



def logout_confirm(request):
    return render(request, 'registration/logout_confirm.html')
#login and logout done
#dont touch above code


#project views start
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'ems/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'ems/project_detail.html', {'project': project})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'ems/add_project.html', {'form': form})

def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'ems/edit_project.html', {'form': form})

def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project_name = project.name  # Get project name before deleting
        project.delete()
        messages.success(request, f'Project "{project_name}" has been deleted.')  # Success message
        return redirect('project_list')
    return render(request, 'ems/delete_project.html', {'project': project})

#project views end




#dummy place holde code, have to work on it

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


