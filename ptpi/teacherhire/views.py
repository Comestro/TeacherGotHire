from django.shortcuts import render
from .models import Subject, Qualification, Teacher, Rating
from ..ptpi.serializers import SubjectSerializer, QualificationSerializer, TeacherSerializer, RatingSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def subjectsInfo(request):
    sub = Subject.objects.all()
    serializer = SubjectSerializer(sub)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
