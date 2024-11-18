from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now

class Subject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    marks = models.IntegerField(default=0)
    status = models.BooleanField(default=True)  
    backlogs = models.CharField(max_length=400, default="No Backlogs")  
    created_at = models.DateTimeField(default=now)  
    updated_at = models.DateTimeField(auto_now=True)  
    def __str__(self):
        return self.title
    
class Skill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.skill_name

class Qualification(models.Model):
    # userid, skill(teacherid, , skillname), 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    skill_name = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True, blank=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    bio = models.TextField(null=True, blank=True)
    experience_year = models.IntegerField(null=True, blank=True)
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE, null=True, blank=True, related_name='qualification')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True, related_name='subject')
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

class Level(models.Model):
    # subjectid
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=400,null=True,blank=True)
    description= models.CharField(max_length=400,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): 
        return self.name
    
class Question(models.Model):
    subject_id = models.IntegerField(null=True,blank=True)
    question = models.CharField(max_length=200,null=True,blank=True)
    answer = models.CharField(max_length=200,null=True,blank=True)
    level= models.ForeignKey(Level, on_delete=models.CASCADE)
    options = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.subject_id
    
class Register(models.Model):
    Fname = models.CharField(max_length=500)
    Lname = models.CharField(max_length=500)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=200)
    contact = models.IntegerField()
    def __str__(self):
        return f"{self.Fname} {self.Lname}"
    
class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.email

class AdminLogin(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.email