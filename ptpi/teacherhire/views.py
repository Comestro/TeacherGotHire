from django.shortcuts import render
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

class RegisterUser(APIView):
    def post(self,request):
        serializer= UserSerializer(data = request.data)

        if not serializer.is_valid():
            return Response({'status':403,'errors': serializer.errors,'message':'Something went wrong '})
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        token_obj, __ =Token.objects.get_or_create(user=user)
        return Response({'status':200,'payload':serializer.data, 'token':str(token_obj) ,'message':'your data is save'})


class SubjectViewSet(viewsets.ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


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

class AdminLoginViewSet(viewsets.ModelViewSet):
    queryset= AdminLogin.objects.all()
    serializer_class=AdminLoginSerializer


