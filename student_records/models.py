from django.db import models
# course model to register courses
class Course(models.Model):

    #add course name(fieldtpye : char) 
    course_name = models.CharField(max_length=100)

    #course code(fieldtpye : char)
    course_code = models.CharField(max_length=10) 

    def __str__(self):
        return self.name
    
# student model to create student  
class Student(models.Model):
    
    #here we type the name of the Student and which have fieldtype : char and has MAX_LENGTH=100
    name = models.CharField(max_length=100)

     # To store type the age of student fieldtype :  int 
    age = models.IntegerField() 

    #manytomany field to assign courses to student 
    courses = models.ManyToManyField(Course) 

    def __str__(self):
        return self.name

# Teacher model to assign  name and course to the teacher
class Teacher(models.Model): 
    #assign teacher name 
    teacher_name = models.CharField(max_length=100) 

    #used manytomany field to assign courses to teacher
    courses = models.ManyToManyField(Course) 
    
    def __str__(self):
        return self.name

