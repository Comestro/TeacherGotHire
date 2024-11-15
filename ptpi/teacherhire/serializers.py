from rest_framework import serializers
from teacherhire.models import Subject, Qualification,Teacher,Rating,Level,Question

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