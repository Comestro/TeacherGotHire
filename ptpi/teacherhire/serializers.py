from rest_framework import serializers
from teacherhire.models import Subject, Qualification,Teacher,Rating,Level,Question,Register,Login, AdminLogin
from django.contrib.auth.models import User
from teacherhire.models import Subject, Qualification,Teacher,Rating,Level,Question,Register,Login,AdminLogin
from  django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

        return user

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'description', 'marks', 'status', 'backlogs', 'created_at', 'updated_at']
    
class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer() 
    qualification = QualificationSerializer()
    subject = SubjectSerializer()
    class Meta:
        model = Teacher
        fields = ['id', 'user', 'bio', 'experience_year', 'qualification', 'subject']


class RatingSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()  # Nested serializer to show teacher details

    class Meta:
        model = Rating
        fields = ['id', 'teacher', 'rating', 'comment']

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = "__all__"

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = "__all__"

class AdminLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminLogin 
        fields = "__all__"
