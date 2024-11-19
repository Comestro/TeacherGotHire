from rest_framework import serializers
from teacherhire.models import Subject, Qualification,Teacher,Rating,Level,Question,Register,Login, AdminLogin
from django.contrib.auth.models import User
from teacherhire.models import Subject, Qualification,Teacher,Rating,Level,Question,Register,Login,AdminLogin
from  django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email',"password"]

    def create(self, validated_data):
        """
        Create a new user and hash the password automatically.
        """
        # Using create_user ensures the password is hashed before saving
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            email=validated_data['password'],
        )
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
        """
        Create and return a new user instance.
        Manually hash the password before saving the user.
        """
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
                
        user.set_password(validated_data['password'])
        user.save() 
        
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate(self, data):
        # Check if the email exists
        email = data.get('email')
        password = data.get('password')

        # Look up the user by email and check the password
        user = authenticate(username=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid email or password, please try again.")

        data['user'] = user
        return data
    email = serializers.EmailField()
    # password = serializers.CharField(write_only=True)

    def validate(self, data):
        # Retrieve username and password from the validated data
        email = data.get('email')
        # password = data.get('password')

        # Try to authenticate the user
        user = authenticate(email=email)

        if not user:
            raise serializers.ValidationError("Invalid credentials, please try again.")

        # Return the user if authenticated
        data['user'] = user
        return data
class AdminLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminLogin 
        fields = "__all__"
