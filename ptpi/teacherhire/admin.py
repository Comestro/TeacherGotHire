from django.contrib import admin
from .models import Subject, Qualification, Teacher, Rating

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'marks', 'status', 'backlogs', 'created_at', 'updated_at']

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):  
    list_display = ['id', 'highest_qualification', 'institution', 'board']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'experience_year', 'qualification', 'subject']

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):  
    list_display = ['teacher', 'rating', 'comment']
