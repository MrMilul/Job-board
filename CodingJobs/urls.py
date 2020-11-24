"""CodingJobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.core import views as v
from apps.job import views as vv
from apps.userprofile.views import dashboard
from django.contrib.auth import views

urlpatterns = [

    path('', v.frontpage, name='frontpage'),
    path('signup/', v.singup, name='signup'),
    path('admin/', admin.site.urls),
    path('logout/', views.LogoutView.as_view(), name="logout"), 
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'), 
    path('jobs/<int:job_id>/', vv.detail_job, name='detail_job'), 
    path('dashboard/', dashboard, name='dashboard')
]

