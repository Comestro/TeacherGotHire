from django.contrib import admin
from django.urls import path, include
from teacherhire.views import (
    SubjectViewSet, QualificationViewSet, TeacherViewSet, RatingViewSet, 
    LevelViewSet, QuestionViewSet,OptionCreateView, RegisterUser,LevelCreateView, LoginUser,OptionViewSet,SkillViewSet,LoginViewSet,RegisterViewSet,SubjectCreateView
    , TeacherViewSet, RatingViewSet,SubjectViewSet,
    LevelViewSet, QuestionViewSet,OptionCreateView, RegisterUser,LevelCreateView,
    LoginUser,OptionViewSet,SkillViewSet,LoginViewSet,RegisterViewSet,SubjectCreateView,
    LevelDeleteView,SubjectDeleteView
    , TeacherViewSet, RatingViewSet, SubjectViewSet,
    LevelViewSet, QuestionViewSet, OptionCreateView, RegisterUser,LevelCreateView,
    LoginUser, OptionViewSet, SkillViewSet, LoginViewSet, RegisterViewSet, SubjectCreateView,
    LevelDeleteView, SubjectDeleteView, TeacherDeleteView, QualificationDeleteView,
    OptionDeleteView, SkillDeleteView, RatingDeleteView, QuestionDeleteView,QuestionCreateView
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
    path('admin/subject/view/', SubjectViewSet.as_view({'get': 'list'}), name='viewsubject'),
    path('admin/subject/create/', SubjectCreateView.as_view(), name='subject-create'),
    path('admin/teacher/view/', TeacherViewSet.as_view({'get': 'list'}), name='teacher'),
    path('admin/subject/<int:pk>/', SubjectDeleteView.as_view(), name='subject-delete'),
    path('admin/level/create/', LevelCreateView.as_view(), name='level-create'),
    path('admin/level/<int:pk>/', LevelDeleteView.as_view(), name='level-delete'),
    path('admin/option/create/', OptionCreateView.as_view(), name='option-create'),
    path('admin/option/<int:pk>/', OptionDeleteView.as_view(), name='option-delete'), 
    path('admin/teacher/<int:pk>/', TeacherDeleteView.as_view(), name='teacher-delete'),
    path('admin/skill/<int:pk>/', SkillDeleteView.as_view(), name='skill-delete'),
    path('admin/rating/<int:pk>/', RatingDeleteView.as_view(), name='rating-delete'),
    path('admin/question/<int:pk>/', QuestionDeleteView.as_view(), name='question-delete'),
    path('admin/question/create/', QuestionCreateView.as_view(), name='question-create'),
    path('admin/qualification/<int:pk>/', QualificationDeleteView.as_view(), name='qualification-delete'),
]
