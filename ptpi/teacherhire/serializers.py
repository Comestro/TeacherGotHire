from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from teacherhire.models import Subject, Qualification, Teacher, Rating, Level, Question, Register, Login, Option, Skill

# User Serializer for Registration and User Profile
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

# Subject Serializer
class SubjectSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True) 
    class Meta:
        model = Subject
        fields = ['id','title', 'description', 'marks', 'status', 'backlogs']

# Qualification Serializer
class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = "__all__"

# Skill Serializer
class SkillSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Skill
        fields = ['id', 'user_id', 'skill_name']

# Teacher Serializer 
class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True) 
    qualification = QualificationSerializer(read_only=True)
    subject = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'bio', 'experience_year', 'qualification', 'subject']
# Rating Serializer
class RatingSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()  # Nested serializer to show teacher details
    class Meta:
        model = Rating
        fields = ['id', 'teacher', 'rating', 'comment']

# Level Serializer
class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"


# Option Serializer
class OptionSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Option
        fields = "__all__"
        
# class UserSerializer(serializers.ModelSerializer):    
    # class Meta:
        # model = User
        # fields = "__all__"
        
# Question Serializer         
class QuestionSerializer(serializers.ModelSerializer):
    option = OptionSerializer(many=True,read_only=True)
    level = LevelSerializer(read_only=True)
    class Meta:
        model = Question
        fields = "__all__"

# Registration Serializer (for User Registration)
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

# Login Serializer (for User Login)
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(username=email, password=password)
        
        if not user:
            raise serializers.ValidationError("Invalid email or password, please try again.")
        
        data['user'] = user
        return data



