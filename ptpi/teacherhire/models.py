from django.db import models

# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    marks = models.IntegerField()
    status = models.BooleanField()
    backlogs = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
