from django.shortcuts import render
from .models import Subject, Qualification, Teacher, Rating
from .serializers import SubjectSerializer, QualificationSerializer, TeacherSerializer, RatingSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def subjects(req):
    sub = Subject.objects.all()
    serializer = SubjectSerializer(sub)
    json_data = JSONRenderer(serializer).render(serializer.data)