from django.contrib import admin
from django.urls import path,include
from teacherhire.views import SubjectViewSet,QualificationViewSet,TeacherViewSet,RatingViewSet,LevelViewSet,QuestionViewSet,RegisterViewSet,LoginViewSet,AdminLoginViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'subjects',SubjectViewSet)
router.register(r"qualifications",QualificationViewSet)
router.register(r"teachers",TeacherViewSet)
router.register(r'ratings',RatingViewSet)
router.register(r'levels',LevelViewSet)
router.register(r'questions',QuestionViewSet)
router.register(r'registers',RegisterViewSet)
router.register(r'login',LoginViewSet)
router.register(r'adminlogin',AdminLoginViewSet)

urlpatterns = [
    path('',include(router.urls)),
]