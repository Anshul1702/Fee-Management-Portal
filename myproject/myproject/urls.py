"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from app1.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome),
    path('login/', login),
    path('logout/', logout),
    path('auth_error/', auth_error),
    path('admin_home/', admin_home),
    path('employee_home/', employee_home),
    path('student_data/', student_data),
    path('employee_data/', employee_data),
    path('search_student/', search_student),
    path('search_student0/', search_student0),
    path('student_reg/', student_reg),
    path('employee_reg/', employee_reg),
    path('edit_student0/', edit_student0),
    path('edit_student/', edit_student),
    path('save_student/', save_student),
    path('delete_student/', delete_student),
    path('delete_student0/', delete_student0),
    path('student_profile/', student_profile),
    path('employee_profile/', employee_profile),
    path('save_employee/', save_employee),
    path('search_employee/', search_employee),
    path('search_employee0/', search_employee0),
    path('edit_employee0/', edit_employee0),
    path('edit_employee/', edit_employee),
    path('delete_employee0/', delete_employee0),
    path('delete_employee/', delete_employee),
    path('admin_profile/', admin_profile),
    path('uploadphoto/', uploadphoto),
    path('uploadphotoadmin/', uploadphotoadmin),
    path('uploadphotoemployee/', uploadphotoemployee),
    path('change_password_admin/', change_password_admin),
    path('change_password_employee/', change_password_employee),
    path('home/', home),
    path('profile/', profile),
    path('student_home/', student_home),
    path('save_student_fees/', save_student_fees),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)