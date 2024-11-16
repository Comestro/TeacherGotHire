from django.shortcuts import render
from rest_framework import viewsets
from teacherhire.models import Subject , Qualification,Teacher,Rating,Level,Question
from teacherhire.serializers import SubjectSerializer,QualificationSerializer,TeacherSerializer,RatingSerializer,LevelSerializer,QuestionSerializer

# Create your views here.
def home(request):
  return render(request,"home.html")
  

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
