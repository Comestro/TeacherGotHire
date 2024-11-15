
from django.contrib import admin
from django.urls import path,include
from ptpi.views import SubjectViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'teacherhire',SubjectViewSet)


urlpatterns = [
    path('',include(router.urls)),
    

]
