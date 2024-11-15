from django.contrib import admin
from django.urls import path
from teacherhire import views

urlpatterns = [
    path('admin/', admin.site.urls),
]
