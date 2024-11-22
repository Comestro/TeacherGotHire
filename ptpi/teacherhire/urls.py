from django.contrib import admin
from django.urls import path, include
from teacherhire.views import (
    SubjectViewSet, QualificationViewSet, TeacherViewSet, RatingViewSet, 
    LevelViewSet, QuestionViewSet, RegisterUser, LoginUser,OptionViewSet,SkillViewSet,LoginViewSet,RegisterViewSet
    )
from rest_framework import routers


router = routers.DefaultRouter()
# router.register(r'subjects',SubjectViewSet)
router.register(r"qualifications",QualificationViewSet)
# router.register(r"teachers",TeacherViewSet)
router.register(r'ratings',RatingViewSet)
router.register(r'levels',LevelViewSet)
router.register(r'questions',QuestionViewSet)  
router.register(r'options',OptionViewSet)
router.register(r'skills',SkillViewSet)
router.register(r'registers',RegisterViewSet)
# router.register(r'login',LoginViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('admin/teacher/view/', TeacherViewSet.as_view({'get': 'list'}), name='teacher'),
    
]
