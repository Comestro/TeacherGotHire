from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from teacherhire.models import Subject ,Qualification,Teacher,Rating,Level,Question,Register,Login,AdminLogin, Option
from teacherhire.serializers import SubjectSerializer,QualificationSerializer,TeacherSerializer,RatingSerializer, LevelSerializer,QuestionSerializer,RegisterSerializer,LoginSerializer,AdminLoginSerializer,UserSerializer, OptionSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import requests
from django.contrib.auth.models import User
from rest_framework.decorators import api_view

# Create your views here.
def home(request):
  return render(request,"home.html")

def dashboard(request):
    return render(request, "admin_panel/dashboard.html")

#teacher
def manage_teacher(request):
    response = requests.get("http://127.0.0.1:8000/api/teachers/").json()
    return render(request, "admin_panel/manage-teacher.html", {'response':response})

@api_view(['DELETE'])
def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    #return redirect('manage_teacher')
    return render(request, "admin_panel/manage-teacher.html")


#Subject
def manage_subject(request):
    response=requests.get("http://127.0.0.1:8000/api/subjects/").json()
    return render(request, "admin_panel/manage-subjects.html",{'response':response})

@api_view(['DELETE'])
def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    return render(request, "admin_panel/manage-subjects.html")

#Qualification
def manage_qualification(request):
    response =requests.get("http://127.0.0.1:8000/api/qualifications/").json()
    return render(request, "admin_panel/manage-qualifications.html",{'response':response})

@api_view(['DELETE'])
def delete_quali(request, pk):
    qualification = get_object_or_404(Qualification, pk=pk)
    qualification.delete()
    return redirect(manage_qualification)
    #return Response({"message": "Qualification deleted successfully"}, status=204)

#rating
def manage_rating(request):
    response=requests.get('http://127.0.0.1:8000/api/ratings/').json()
    return render(request, "admin_panel/manage-rating.html",{'response':response})

@api_view(['DELETE'])
def delete_rating(request, pk):
    rating = get_object_or_404(Rating, pk=pk)
    rating.delete()
    # return redirect('manage_rating')
    #redirect(manage_rating)
    return render(request, "admin_panel/manage-rating.html")

def manage_questions(request):
    data = {}
    data['response']=requests.get('http://127.0.0.1:8000/api/questions/').json()
    data['options']=requests.get('http://127.0.0.1:8000/api/options/').json()
    return render(request, "admin_panel/manage-question.html",data)

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
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

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

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class=OptionSerializer

class RegisterViewSet(viewsets.ModelViewSet):
    queryset= Register.objects.all()
    serializer_class=RegisterSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset= Login.objects.all()
    serializer_class=LoginSerializer

class AdminLoginViewSet(viewsets.ModelViewSet):
    queryset= AdminLogin.objects.all()
    serializer_class=AdminLoginSerializer
