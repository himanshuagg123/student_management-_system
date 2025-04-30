from django.shortcuts import render

from .models import Student,Course,Teacher
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
import json
# from .serializers import StudentSerializer

@api_view(['GET']) #function based api
def Student_Details(request):
    students_list = Student.objects.all() # Fetching all students from the database

    student_data = [] 
    for student in students_list:
        student_data.append({
            'id': student.id,
            'name': student.name,
            'age': student.age,
            'email': student.email,
            'courses': list(student.courses.values('id', 'course_name'))  
    
    })
        # Return the list of students as a Response object
    return Response(student_data)
class StudentDetailsPost(APIView): #class based api
    def post(self, request): #request method psot
        if request.method == 'POST': 
            data = json.loads(request.body.decode('utf-8')) 

            Student_Create = Student.objects.create(name=data['name'],age=data['age'],email=data['email'])

            if 'courses' in data:
                courses = Course.objects.filter(id__in=data['courses'])  # Get the courses by ID
                Student_Create.courses.set(courses) 

            return Response({'id': Student_Create.id, 'name': Student_Create.name , 'age': Student_Create.age, 'email': Student_Create.email, 'courses': [course.id for course in Student_reate.courses.all()]},status=201)

# Create your views here.

@api_view(['GET']) #function based api
def Course_Details(request):
    course_list = Course.objects.all() # Fetching all students from the database

    Course_data = [] 
    for course in course_list:
        Course_data.append({
            'id': course.id,
            'course_name': course.course_name,
            'course_code': course.course_code,
           
    
    })
        # Return the list of students as a Response object
    return Response(Course_data)

class CoursetDetailsPost(APIView): #class based api
    def post(self, request): #request method psot
        if request.method == 'POST': 
            data = json.loads(request.body.decode('utf-8')) 

            Course_Create = Course.objects.create(course_name=data['course_name'],course_code=data['course_code'])

            return Response({'id': Course_Create.id, 
                             'course_name': Course_Create.course_name, 
                             'Course_code': Course_Create.course_code}, status=201)

@api_view(['GET'])
def Teacher_Details(request):
    teacher_list = Teacher.objects.all() # Fetching all students from the database

    teacher_data = [] 
    for teacher in teacher_list:
        teacher_data.append({
            'id': teacher.id,
            'name': teacher.teacher_name,
           
            # 'courses': list(student.courses.values('id', 'course_name'))  
    
    })
        # Return the list of students as a Response object
    return Response(teacher_data)

class teacherDetailsPost(APIView): #class based api
    def post(self, request): #request method psot
        if request.method == 'POST': 
            data = json.loads(request.body.decode('utf-8')) 

            Teacher_Create = Teacher.objects.create(teacher_name=data['teacher_name'])

            # if 'courses' in data:
            #     courses = Course.objects.filter(id__in=data['courses'])  # Get the courses by ID
            #     Student_Create.courses.set(courses) 

            return Response({'id': Teacher_Create.id, 'teacher_name': Teacher_Create.teacher_name},status=201)
