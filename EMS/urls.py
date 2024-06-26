from django.urls import path
from . import views

urlpatterns = [
    #dashboard url
    path('', views.dashboard, name='dashboard'),
    #employees urls
    path('employees/', views.employee_list, name='employee_list'),
    path('add/', views.add_employee, name='add_employee'),
    path('<int:pk>/', views.employee_detail, name='employee_detail'),       #dont touch this
    path('<int:pk>/update/', views.update_employee, name='update_employee'),
    path('<int:pk>/delete/', views.delete_employee, name='delete_employee'),
    
    #log out confirm path
    # path('logout_confirm/', views.logout_confirm, name='logout_confirm'),
    path('logout_confirm/', views.logout_confirm, name='logout_confirm'),
    
        
    #projects urls
    path('projects/', views.project_list, name='project_list'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('projects/delete/<int:project_id>/', views.delete_project, name='delete_project'),
    # done
      
#    leaves url
    path('leaves/', views.leave_list, name='leave_list'),
    path('leaves/apply/', views.apply_leave, name='apply_leave'),
    path('leaves/<int:pk>/approve/', views.approve_leave, name='approve_leave'),
    path('leaves/<int:pk>/reject/', views.reject_leave, name='reject_leave'),
]