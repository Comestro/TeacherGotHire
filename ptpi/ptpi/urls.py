from django.contrib import admin
from django.urls import path, include
from teacherhire.views import home, dashboard, teacher, subject, qualification, rating

urlpatterns = [
    path("home/", home),
    path("admin/dashboard/", dashboard, name='admin.dashboard'),
    path("admin/manage/teacher/", teacher, name='admin.manage.teacher'),
    path("admin/manage/subject/", subject, name='admin.manage.subject'),
    path("admin/manage/rating/", rating, name='admin.manage.rating'),
    path("admin/manage/qualification/", qualification, name='admin.manage.qualification'),
    path('admin/', admin.site.urls),
    path("api/",include('teacherhire.urls')),
]
