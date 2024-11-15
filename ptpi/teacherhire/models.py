from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now


class Subject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    marks = models.IntegerField(default=0)
    status = models.BooleanField(default=True)  # Default set for status
    backlogs = models.CharField(max_length=400, default="No Backlogs")  # Default for backlogs
    created_at = models.DateTimeField(default=now)  # Ensures valid datetime default
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated

    def __str__(self):
        return self.title


class Qualification(models.Model):
    highest_qualification = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        choices=[
            ("B.Tech", "B.Tech"), ("M.Tech", "M.Tech"), ("PhD", "PhD"),
            ("BSc", "BSc"), ("MSc", "MSc"), ("BA", "BA"),
            ("MA", "MA"), ("MBA", "MBA"), ("B.Ed", "B.Ed"), ("M.Ed", "M.Ed")
        ]
    )
    institution = models.CharField(max_length=200, null=True, blank=True)
    board = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        choices=[('BSEB', 'BSEB'), ('CBSE', 'CBSE'), ('ICSE', 'ICSE')]
    )

    def __str__(self):
        return self.highest_qualification or "Unknown Qualification"


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    experience_year = models.IntegerField(null=True, blank=True)
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username if self.user else "Unknown Teacher"


class Rating(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return f"Rating: {self.rating or 'N/A'}"
