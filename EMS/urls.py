from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('employees/', views.employee_list, name='employee_list'),
    path('add/', views.add_employee, name='add_employee'),
    path('<int:pk>/', views.employee_detail, name='employee_detail'),       #dont touch this
    path('<int:pk>/update/', views.update_employee, name='update_employee'),
    path('<int:pk>/delete/', views.delete_employee, name='delete_employee'),
    
    #log out confirm path
    path('logout_confirm/', views.logout_confirm, name='logout_confirm'),
    
    #not done
    path('projects/', views.project_list, name='project_list'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('projects/<int:pk>/delete/', views.delete_project, name='delete_project'),
    
    
    
    # dummy placceholder code, not working
    #need to fix this
    path('leaves/', views.leave_list, name='leave_list'),
    path('leaves/apply/', views.leave_apply, name='leave_apply'),
]
