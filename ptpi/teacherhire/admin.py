from django.contrib import admin
from .models import Subject, Qualification, Teacher, Rating,Register, Question

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'marks', 'status', 'backlogs', 'created_at', 'updated_at']

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'qualification_name', 'institute', 'percentage']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'experience_year', 'qualification', 'display_subjects']
    def display_subjects(self, obj):
        return ", ".join([subject.title for subject in obj.subject.all()])
    display_subjects.short_description = 'Subjects'

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):  
    list_display = ['teacher', 'rating', 'comment']

@admin.register(Register)
class RatingAdmin(admin.ModelAdmin):  
    list_display = ['Fname', 'Lname', 'email','password','contact']

@admin.register(Question)
class Question(admin.ModelAdmin):
    list_display = ['subject_id', 'question', 'answer', 'level']