from django.contrib import admin
from django.urls import path, include
from teacherhire.views import home, dashboard, teacher

urlpatterns = [
    path("home/", home),
    path("admin/dashboard/", dashboard, name='admin.dashboard'),
    path("admin/manage/teacher/", teacher, name='admin.manage.teacher'),
    path('admin/', admin.site.urls),
    path("api/",include('teacherhire.urls')),

]
