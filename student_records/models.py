from django.db import models
from django.contrib.auth.models import User


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
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    teacher_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100, unique=True, default='no-email@example.com')
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.teacher_name

# models.py

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    marks_obtained = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.course.course_name} - {self.marks_obtained}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField()

    def __str__(self):
        return f"{self.student.name} - {self.date} - {'Present' if self.is_present else 'Absent'}"
