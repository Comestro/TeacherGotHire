from django.shortcuts import render
from rest_framework import viewsets
from teacherhire.models import Subject
from ptpi.serializers import SubjectSerializer

# Create your views here.
class SubjectViewSet(viewsets.ModelViewSet):
    queryset= Subject.objects.all()
    serializer_class=SubjectSerializer
