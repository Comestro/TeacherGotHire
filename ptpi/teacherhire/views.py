from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from teacherhire.models import Subject , Qualification,Teacher,Rating,Level,Question,Register,Login,AdminLogin
from teacherhire.serializers import SubjectSerializer,QualificationSerializer,TeacherSerializer,RatingSerializer,\
    LevelSerializer,QuestionSerializer,RegisterSerializer,LoginSerializer,AdminLoginSerializer,UserSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from teacherhire.models import Subject , Qualification,Teacher,Rating,Level,Question,Register,Login
from teacherhire.serializers import SubjectSerializer,QualificationSerializer,TeacherSerializer,RatingSerializer,LevelSerializer,QuestionSerializer,RegisterSerializer,LoginSerializer, AdminLoginSerializer
from .models import Teacher, AdminLogin
import requests
from rest_framework.decorators import api_view


# Create your views here.
def home(request):
  return render(request,"home.html")

def dashboard(request):
    return render(request, "admin_panel/dashboard.html")

def manage_teacher(request):
    response = requests.get("http://127.0.0.1:8000/api/teachers/").json()
    return render(request, "admin_panel/manage-teacher.html", {'response':response})

def manage_subject(request):
    response=requests.get("http://127.0.0.1:8000/api/subjects/").json()
    return render(request, "admin_panel/manage-subjects.html",{'response':response})

def manage_qualification(request):
    response =requests.get("http://127.0.0.1:8000/api/qualifications/").json()
    return render(request, "admin_panel/manage-qualifications.html",{'response':response})

def rating(request):
    return render(request, "admin_panel/manage-rating.html")

class RegisterUser(APIView):
    def post(self,request):
        serializer= UserSerializer(data = request.data)

        if not serializer.is_valid():
            return Response({'status':403,'errors': serializer.errors,'message':'Something went wrong '})
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        token_obj, __ =Token.objects.get_or_create(user=user)
        return Response({'status':200,'payload':serializer.data, 'token':str(token_obj) ,'message':'your data is save'})

def manage_rating(request):
    response=requests.get('http://127.0.0.1:8000/api/ratings/').json()
    return render(request, "admin_panel/manage-rating.html",{'response':response})


@api_view(['DELETE'])
def delete_rating(req, pk):
    rating = get_object_or_404(Rating, pk=pk)
    rating.delete()
    redirect(manage_rating)
  

class SubjectViewSet(viewsets.ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    queryset= Subject.objects.all()
    serializer_class=SubjectSerializer

class QualificationViewSet(viewsets.ModelViewSet):
    queryset= Qualification.objects.all()
    serializer_class=QualificationSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

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

class AdminLoginViewSet(viewsets.ModelViewSet):
    queryset= AdminLogin.objects.all()
    serializer_class=AdminLoginSerializer
