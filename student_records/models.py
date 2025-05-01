from django.db import models

# Create your models here.

class Course(models.Model): #course model
    course_name = models.CharField(max_length=100) #add course name(fieldtpye : char)
    course_code = models.CharField(max_length=10) #course code(fieldtpye : char)

    def __str__(self):
        return self.name
class Student(models.Model):
    name = models.CharField(max_length=100) #here we type the name of the Student and which have fieldtype : char and has MAX_LENGTH=100
    age = models.IntegerField((""))  # To stor type the age of student fieldtype :  int
    email = models.EmailField()
    courses = models.ManyToManyField(Course) #manytomany field to assign courses to student 

    def __str__(self):
        return self.name


class Teacher(models.Model): #teacher model to assign  name and course to the teacher
    teacher_name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course) #used manytomany field to assign courses to teacher
    
    def __str__(self):
        return self.name

