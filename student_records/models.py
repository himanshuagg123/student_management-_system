from django.db import models

# Course model
class Course(models.Model):
    course_name = models.CharField(max_length=100,unique=True)
    course_code = models.CharField(max_length=10, unique=True)  # Ensure unique courses

    def __str__(self):
        return self.course_name

# Student model
class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)  # Unique student identifier
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

# Teacher model
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100,unique=True)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.teacher_name
