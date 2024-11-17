from rest_framework import serializers
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
        fields = "__all__"
    
class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        user_name = serializers.CharField(source='user.name')
        qualification = serializers.CharField(source='qualification.highest_qualification')
        subject = serializers.CharField(source='subject.name')

        fields = "__all__"

class RatingSerializer(serializers.ModelSerializer):
     class Meta:
         model = Rating
         teacher = serializers.CharField(source='teacher.user.name')
         fields = ['teacher', 'rating', 'comment']

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
