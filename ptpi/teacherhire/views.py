from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from teacherhire.models import Subject ,Qualification,Teacher,Rating,Level,Question,Register,Login, Option, Skill
from teacherhire.serializers import SubjectSerializer,QualificationSerializer,TeacherSerializer,RatingSerializer, LevelSerializer,QuestionSerializer,RegisterSerializer,LoginSerializer,UserSerializer, OptionSerializer, SkillSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
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
    response = requests.get("http://127.0.0.1:8000/api/admin/teachers/").json()
    return render(request, "admin_panel/manage-teacher.html", {'response':response})

@api_view(['DELETE','PUT'])
def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    #return redirect('manage_teacher')
    return render(request, "admin_panel/manage-teacher.html")


def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == 'POST':
        serializer = TeacherSerializer(teacher, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return redirect('manage_teacher')
        return Response(serializer.errors, status=400)

    else:
        serializer = TeacherSerializer(teacher)
        return render(request, "admin_panel/manage-teacher.html", {'form': serializer.data})



#Subject
def manage_subject(request):
    response=requests.get("http://127.0.0.1:8000/api/admin/subjects/").json()
    return render(request, "admin_panel/manage-subjects.html",{'response':response})

@api_view(['DELETE'])
def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    return render(request, "admin_panel/manage-subjects.html")

#Qualification
def manage_qualification(request):
    response =requests.get("http://127.0.0.1:8000/api/admin/qualifications/").json()
    return render(request, "admin_panel/manage-qualifications.html",{'response':response})

@api_view(['DELETE'])
def delete_quali(request, pk):
    qualification = get_object_or_404(Qualification, pk=pk)
    qualification.delete()
    return redirect(manage_qualification)
    #return Response({"message": "Qualification deleted successfully"}, status=204)

#rating
def manage_rating(request):
    response=requests.get('http://127.0.0.1:8000/api/admin/ratings/').json()
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
    data['response']=requests.get('http://127.0.0.1:8000/api/admin/questions/').json()
    data['options']=requests.get('http://127.0.0.1:8000/api/options/').json()
    return render(request, "admin_panel/manage-question.html",data)

@api_view(['DELETE'])
def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    # return redirect('manage_rating')
    #redirect(manage_rating)
    return render(request, "admin_panel/manage-question.html")

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'status': 400,
                'errors': serializer.errors,
                'message': 'Invalid data provided.'
            }, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = serializer.save()
        except IntegrityError as e:
            return Response({
                'status': 400,
                'message': 'Username or email already exists.',
                'errors': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)        
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({
            'status': 200,
            'payload': serializer.data,
            'token': access_token,
            'message': 'User registered successfully.'
        }, status=status.HTTP_201_CREATED)
        
        
class LoginUser(APIView):
    def post(self, request):        
        email = request.data.get("email")
        password = request.data.get("password")        
        if not email or not password:
            return Response({
                'status': 400,
                'message': 'Email and password are required.'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({
                'status': 401,
                'message': 'Invalid credentials, please try again.'
            }, status=status.HTTP_401_UNAUTHORIZED)
        if not user.is_active:
           raise AuthenticationFailed("Account is disabled, please contact support.")
       
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)            

            return Response({
                'status': 200,                
                'message': 'Login successful.',
                'token': access_token,
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'status': 401,
                'message': 'Invalid credentials, please try again.'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
class TeacherCreateView(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"error": "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        
        if Teacher.objects.filter(user=request.user).exists():
            return Response({"error": "Teacher profile already exists."}, status=status.HTTP_400_BAD_REQUEST)
        data = request.data.copy()
        data['user'] = request.user.id 

        serializer = TeacherSerializer(data=data)
        if serializer.is_valid():
            try:
                teacher = serializer.save(user=request.user)  
                if 'subject' in request.data:
                    teacher.subject.set(request.data.get('subject'))  
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                return Response({"error": "Database integrity error", "details": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
# class TeacherCreateView(APIView):
#     def post(self, request):
#         serializer = TeacherSerializer(data=request.data)
#         if serializer.is_valid():
#             teacher = serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubjectCreateView(APIView):
    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():            
            Subject = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LevelCreateView(APIView):
    def post(self, request):
        serializer = LevelSerializer(data=request.data)
        if serializer.is_valid():            
            Level = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OptionCreateView(APIView):
    def post(self,request):
        serializer = OptionSerializer(data=request.data)
        if serializer.is_valid():
            Option = serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
class QuestionCreateView(APIView):
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            Option = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SkillCreateView(APIView):
    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            Skill = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
class QualificationCreateView(APIView):
    def post(self, request):
        serializer = QualificationSerializer(data=request.data)
        if serializer.is_valid():
            Qualification = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RatingCreateView(APIView):
    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            Rating = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SubjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset= Subject.objects.all()
    serializer_class=SubjectSerializer

class QualificationViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset= Qualification.objects.all().select_related('user_id')
    serializer_class=QualificationSerializer

class TeacherViewSet(viewsets.ModelViewSet):    
    permission_classes = [IsAuthenticated]
    queryset = Teacher.objects.select_related('user', 'qualification').prefetch_related('subject')
    serializer_class = TeacherSerializer

class RatingViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset= Rating.objects.all().select_related('teacher')
    serializer_class=RatingSerializer

class LevelViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset= Level.objects.all().select_related('subject_id')
    serializer_class=LevelSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset= Question.objects.all().select_related('subject_id')
    serializer_class=QuestionSerializer

class OptionViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Option.objects.all().select_related('question')
    serializer_class=OptionSerializer
    
class SkillViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Skill.objects.all().select_related('user_id')
    serializer_class=SkillSerializer

class RegisterViewSet(viewsets.ModelViewSet): 
    queryset= Register.objects.all()
    serializer_class=RegisterSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset= Login.objects.all()
    serializer_class=LoginSerializer


