from django.urls import path, include
from teacherhire.views import (
    SubjectViewSet, QualificationViewSet, TeacherViewSet, RatingViewSet, 
    LevelViewSet, QuestionViewSet, RegisterUser, LoginUser, AdminLoginViewSet
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'subjects', SubjectViewSet)
router.register(r"qualifications", QualificationViewSet)
router.register(r"teachers", TeacherViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'levels', LevelViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'adminlogin', AdminLoginViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
]
