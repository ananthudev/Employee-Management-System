# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .models import Employee, Project, Leave
from .forms import EmployeeForm, ProjectForm, LeaveForm
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.db.models import Count  #for dashboard




# dashboard render
# @login_required
# def dashboard(request):
#     return render(request, 'ems/dashboard.html')


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
# def logout(request):
#     auth_logout(request)
#     return redirect('login')



# def logout_confirm(request):
#     return render(request, 'registration/logout_confirm.html')
def logout_confirm(request):
    auth_logout(request)
    return redirect('login')
#login and logout done
#dont touch above code - Dev, else you will cry

@login_required
#project views start
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'ems/project_list.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'ems/project_detail.html', {'project': project})

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'ems/add_project.html', {'form': form})

@login_required
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

# def delete_project(request, pk):
#     project = get_object_or_404(Project, pk=pk)
#     if request.method == 'POST':
#         project_name = project.name  # Get project name before deleting
#         project.delete()
#         messages.success(request, f'Project "{project_name}" has been deleted.')  # Success message
#         return redirect('project_list')
#     return render(request, 'ems/delete_project.html', {'project': project})

# @login_required
# def delete_project(request):
#     return render(request, 'ems/delete_project.html')

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':
        # If method is POST, delete the project
        project.delete()
        return redirect('project_list')  # Redirect to project list after deletion

    
    return render(request, 'ems/delete_project.html', {'project': project})
    

#project views end

#dummy place holder code, have to work on it
# leave view start
@csrf_exempt
@login_required
def leave_list(request):
    leaves = Leave.objects.all()
    return render(request, 'ems/leave_list.html', {'leaves': leaves})

@csrf_exempt
@login_required
def apply_leave(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leave_list')
    else:
        form = LeaveForm()
    return render(request, 'ems/apply_leave.html', {'form': form})


@login_required
def approve_leave(request, pk):
    leave = get_object_or_404(Leave, pk=pk)
    leave.status = 'approved'
    leave.save()
    return redirect('leave_list')

@csrf_exempt
@login_required
def reject_leave(request, pk):
    leave = get_object_or_404(Leave, pk=pk)
    leave.status = 'rejected'
    leave.save()
    return redirect('leave_list')

@csrf_exempt
@login_required
def dashboard(request):
    # Employee Stats
    total_employees = Employee.objects.count()
    department_stats = Employee.objects.values('department').annotate(count=Count('department'))

    # Project Stats
    total_projects = Project.objects.count()
    projects_pending = Project.objects.filter(status='pending').count()
    projects_inprogress = Project.objects.filter(status='inprogress').count()
    projects_completed = Project.objects.filter(status='completed').count()

    # Leave Stats
    leaves_pending = Leave.objects.filter(status='pending').count()
    leaves_approved = Leave.objects.filter(status='approved').count()
    leaves_rejected = Leave.objects.filter(status='rejected').count()

    context = {
        'total_employees': total_employees,
        'department_stats': department_stats,
        'total_projects': total_projects,
        'projects_pending': projects_pending,
        'projects_inprogress': projects_inprogress,
        'projects_completed': projects_completed,
        'leaves_pending': leaves_pending,
        'leaves_approved': leaves_approved,
        'leaves_rejected': leaves_rejected,
    }
    return render(request, 'ems/dashboard.html', context)
