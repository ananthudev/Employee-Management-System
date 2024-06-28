from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
# from ems.views import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'), #dont touch this
    # path('logout/', logout, name='logout'),
    path('', include('ems.urls')),
]