from rest_framework import serializers
from django.contrib.auth.models import User
<<<<<<< HEAD
from teacherhire.models import Subject, Qualification,Teacher,Rating,Level,Question,Register,Login,AdminLogin, Option, Skill
from  django.contrib.auth.models import User
from django.contrib.auth import authenticate
=======
from django.contrib.auth import authenticate
from teacherhire.models import Subject, Qualification, Teacher, Rating, Level, Question, Register, Login,\
      AdminLogin, Option, Skill
>>>>>>> 932021b1637b098054eb1e368f729f53441a1ebe

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
    class Meta:
        model = Subject
        fields = ['id', 'title', 'description', 'marks', 'status', 'backlogs', 'created_at', 'updated_at']

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

<<<<<<< HEAD

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer() 
    qualification = QualificationSerializer() 
    subject = SubjectSerializer(many=True)  
=======
# Teacher Serializer
class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested serializer, read-only
    qualification = QualificationSerializer(read_only=True)  # Nested serializer, read-only
    subject = SubjectSerializer(read_only=True)  # Nested serializer, read-only
>>>>>>> 932021b1637b098054eb1e368f729f53441a1ebe

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'bio', 'experience_year', 'qualification', 'subject']

<<<<<<< HEAD
=======
# Rating Serializer
class RatingSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()  # Nested serializer to show teacher details
>>>>>>> 932021b1637b098054eb1e368f729f53441a1ebe


class RatingSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()  
    class Meta:
        model = Rating
        fields = ['id', 'teacher', 'rating', 'comment']

# Level Serializer
class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"

# Question Serializer
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

# Option Serializer
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = "__all__"

<<<<<<< HEAD

=======
# Registration Serializer (for User Registration)
>>>>>>> 932021b1637b098054eb1e368f729f53441a1ebe
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate_email(self, value):
        """Ensure email is unique."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        """Create and return a new user instance with hashed password."""
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])  # Hash the password before saving
        user.save()
        return user

# Login Serializer (for User Login)
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        # Authenticate using email as username
        user = authenticate(username=email, password=password)
        
        if not user:
            raise serializers.ValidationError("Invalid email or password, please try again.")
        
        data['user'] = user  # Add the user to the validated data
        return data

# AdminLogin Serializer (for Admin Login)
class AdminLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminLogin
        fields = "__all__"
