from django.db import models

# Course model
class Course(models.Model):
    course_name = models.CharField(max_length=100, unique=True)
    course_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.course_name

# Student model with roll_number instead of student_id
class Student(models.Model):
    roll_number = models.CharField(max_length=20, unique=True,default="0000")  # Changed to roll_number
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

# Teacher model
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100, unique=True,default='no-email@example.com')
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.teacher_name
