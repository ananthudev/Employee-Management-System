from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/logout/confirm/', auth_views.LogoutView.as_view(template_name='registration/logout_confirm.html'), name='logout_confirm'),
    path('', include('ems.urls')),
]
