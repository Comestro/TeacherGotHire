from rest_framework import serializers
from teacherhire.models import Subject, Qualification,Teacher,Rating,Level,Question,Register,Login
from django.contrib.auth.models import User

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
    
class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field = 'username'
    )  
    qualification = serializers.SlugRelatedField(
        queryset=Qualification.objects.all(),
        slug_field='highest_qualification'  # Display 'highest_qualification' in dropdown
    )
    subject = serializers.SlugRelatedField(
        queryset=Subject.objects.all(),
        slug_field='title'  # Display 'title' in dropdown
    )
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
