from rest_framework import serializers
from teacherhire.models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
    
# class QualificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Qualification
#         fields = ['id', 'highest_qualification', 'institution', ]

# # Create your serializers here.
# class TeacherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Teacher
#         user_name = serializers.CharField(source='user.name')
#         qualification = serializers.CharField(source='qualification.highest_qualification')
#         subject = serializers.CharField(source='subject.name')

#         fields = ['user_name','bio', 'experience_year', 'qualification', 'subject']

# class RatingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Rating
#         teacher = serializers.CharField(source='teacher.user.name')
#         fields = ['teacher', 'rating', 'comment']