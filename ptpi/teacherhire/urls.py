from django.contrib import admin
from django.urls import path, include
from teacherhire.views import (
    QualificationViewSet, TeacherViewSet, RatingViewSet,
    LevelViewSet, QuestionViewSet,OptionCreateView, RegisterUser,LevelCreateView,
    LoginUser,OptionViewSet,SkillViewSet,LoginViewSet,RegisterViewSet,SubjectCreateView
    )
from rest_framework import routers


router = routers.DefaultRouter()
#router.register(r'subjects',SubjectViewSet)
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
    path('admin/subject/create/', SubjectCreateView.as_view(), name='subject-create'),
    path('admin/level/create/', LevelCreateView.as_view(), name='level-create'),
    path('admin/option/create/', OptionCreateView.as_view(), name='option-create'),
]
