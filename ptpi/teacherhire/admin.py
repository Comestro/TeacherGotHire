from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc']
    
@admin.register(Qualification)
class Qualification(admin.ModelAdmin):
    list_display = ['id', 'highest_qualification', 'institution', 'board']
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'experience_year', 'qualification', 'subject']

@admin.register(Rating)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'rating', 'comment']