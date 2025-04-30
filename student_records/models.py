from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100) #here we type the name of the Student and which have fieldtype : char and has MAX_LENGTH=100
    age = models.IntegerField((""))  # To stor type the age of student fieldtype :  int
    email = models.EmailField()
