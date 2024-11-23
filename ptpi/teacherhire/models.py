from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now


# subject model
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
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    skill_name = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.skill_name

class Qualification(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    qualification_name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        choices=[
            ("B.Tech", "B.Tech"), ("M.Tech", "M.Tech"), ("PhD", "PhD"),
            ("BSc", "BSc"), ("MSc", "MSc"), ("BA", "BA"),
            ("MA", "MA"), ("MBA", "MBA"), ("B.Ed", "B.Ed"), ("M.Ed", "M.Ed")
        ]
    )
    institute = models.CharField(max_length=200, null=True, blank=True)
    percentage = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.qualification_name 


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    bio = models.TextField(null=True, blank=True)
    experience_year = models.IntegerField(null=True, blank=True)
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE, null=True, blank=True, related_name='qualification')
    subject = models.ManyToManyField(Subject, related_name='teachers') 
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
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=400,null=True,blank=True)
    description= models.CharField(max_length=400,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): 
        return self.name
    
class Question(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = models.CharField(max_length=200, null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.question
    
class Option(models.Model):
    question = models.ForeignKey(Question, related_name="options", on_delete=models.CASCADE)  # Multiple options for each question
    option = models.CharField(max_length=200, null=True, blank=True)  # The text of the option
    is_correct = models.BooleanField(default=False)  # Mark the correct answer (optional)

    def __str__(self):
        return self.option

    
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
    