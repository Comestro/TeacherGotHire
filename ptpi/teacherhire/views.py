from django.shortcuts import render
from rest_framework import viewsets
from teacherhire.models import Subject , Qualification,Teacher,Rating,Level,Question,Register,Login
from teacherhire.serializers import SubjectSerializer,QualificationSerializer,TeacherSerializer,RatingSerializer,LevelSerializer,QuestionSerializer,RegisterSerializer,LoginSerializer

# Create your views here.
def home(request):
  return render(request,"home.html")

def dashboard(request):
    return render(request, "admin_panel/dashboard.html")

def teacher(request):
    return render(request, "admin_panel/manage-teacher.html")

def subject(request):
    return render(request, "admin_panel/manage-subjects.html")

def qualification(request):
    return render(request, "admin_panel/manage-qualifications.html")

def rating(request):
    return render(request, "admin_panel/manage-rating.html")
  

class SubjectViewSet(viewsets.ModelViewSet):
    queryset= Subject.objects.all()
    serializer_class=SubjectSerializer

class QualificationViewSet(viewsets.ModelViewSet):
    queryset= Qualification.objects.all()
    serializer_class=QualificationSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset= Teacher.objects.all()
    serializer_class=TeacherSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset= Rating.objects.all()
    serializer_class=RatingSerializer

class LevelViewSet(viewsets.ModelViewSet):
    queryset= Level.objects.all()
    serializer_class=LevelSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset= Question.objects.all()
    serializer_class=QuestionSerializer

class RegisterViewSet(viewsets.ModelViewSet):
    queryset= Register.objects.all()
    serializer_class=RegisterSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset= Login.objects.all()
    serializer_class=LoginSerializer
