from django.shortcuts import render

from .models import Student,Course,Teacher
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from .serializers import StudentSerializer,CourseSerializer,TeacherSerializer

# API to get the list of students
  
@api_view(['GET'])  # function-based GET with serializer
def Student_Details(request):
    students_list = Student.objects.all()
    serializer = StudentSerializer(students_list, many=True)
    return Response(serializer.data)

# API to post the student details
class StudentDetailsPost(APIView):  # class-based POST with serializer
    def post(self, request):
        serializer = StudentSerializer(data=request.data) # This create a new instances of StudentSerializer with the data recieved from client
        if serializer.is_valid(): # it checks the condition if the data recieved is valid according to the of rules of StudentSerializer if yes it store the data 
            student = serializer.save()
            return Response(StudentSerializer(student).data, status=201)
        return Response(serializer.errors, status=400) # here if rules are not follwed it showes the error 404   
    
# API to get the list of courses  
 
@api_view(['GET'])  # function-based GET
def Course_Details(request):
    course_list = Course.objects.all() 
    serializer = CourseSerializer(course_list, many=True) # call CourseSerializer and show the response in jason format
    return Response(serializer.data)

# API to post the courses  

class CoursetDetailsPost(APIView):  # class-based POST with serializer
    def post(self, request):
        serializer = CourseSerializer(data=request.data) # This create a new instances of CourseSerializer with the data recieved from client
        if serializer.is_valid(): # it checks the condition if the data recieved is valid according to the of rules of CourseSerializer if yes it store the data 
            course = serializer.save()
            return Response(CourseSerializer(course).data, status=201) # if serializer rules are followed show status=201 and data post
        return Response(serializer.errors, status=400) # here if rules are not follwed it showes the error 404  
     
# API to get the list of teachers 

@api_view(['GET'])  # function-based GET
def Teacher_Details(request):
    teacher_list = Teacher.objects.all()
    serializer = TeacherSerializer(teacher_list, many=True)
    return Response(serializer.data)

# API to post teacher_details 

class TeacherDetailsPost(APIView):  # class-based POST with serializer
    def post(self, request):
        serializer = TeacherSerializer(data=request.data) # This create a new instances of TeacherSerializer with the data recieved from client
        if serializer.is_valid():# it checks the condition if the data recieved is valid according to the of rules of TeacherSerializer if yes it store the data 
            teacher = serializer.save()
            return Response(TeacherSerializer(teacher).data, status=201) # if serializer rules are followed show status=201 and data post
        return Response(serializer.errors, status=400) # here if rules are not follwed it showes the error 404  
     