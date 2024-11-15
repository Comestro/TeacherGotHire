from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.name
    
class Qualification(models.Model):
    highest_qualification = models.CharField(max_length=200, null=True, blank=True, choices=( ("B.Tech", "B.Tech"),("M.Tech", "M.Tech"),("PhD", "PhD"),("BSc", "BSc"),("MSc", "MSc"),("BA", "BA"),("MA", "MA"),("MBA", "MBA"),("B.Ed", "B.Ed"),("M.Ed", "M.Ed")))
    institution = models.CharField(max_length=200, null=True, blank=True)
    board = models.CharField(max_length=50, choices=(('BSEB', 'BSEB'), ('CBSE','CBSE'), ('ICSE', 'ICSE')))

    def __str__(self):
        return self.highest_qualification

# Create your models here.
class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    experience_year = models.IntegerField(null=True, blank=True)
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Rating(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    comment = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.rating
