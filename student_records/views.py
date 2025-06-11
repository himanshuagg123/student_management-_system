from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Student, Course, Teacher,Mark,Attendance
from .serializers import StudentSerializer, CourseSerializer, TeacherSerializer,MarkSerializer,AttendanceSerializer
from django.db import IntegrityError

# List & Create Views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Student, Course, Teacher
from .serializers import StudentSerializer, CourseSerializer, TeacherSerializer
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from django.http import JsonResponse
# from rest_framework.permissions import AllowAny, IsAuthenticate
from django.http import HttpResponse
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User


class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        
        validation_error = self.validate_roll_number(request.data.get('roll_number'))
        if validation_error:
            return Response(
                {"error": validation_error},
                status=status.HTTP_400_BAD_REQUEST
            )

        # If no validation errors, proceed with saving the student
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save()
            return Response(StudentSerializer(student).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def validate_roll_number(self, roll_number):
       
        if Student.objects.filter(roll_number=roll_number).exists():
            return ("A student with this roll number already exists in the database.")
        return None

class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        validation_error = self.validate_course(request.data.get('course_code'))
        if validation_error:
            return Response(
                {"error": validation_error},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            course = serializer.save()
            return Response(CourseSerializer(course).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def validate_course(self, course_code):
        
        if Course.objects.filter(course_code=course_code).exists():
            return "A course with this course_code already exists in the database."
        return None

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        validation_error = self.validate_email(request.data.get('email_id'))
        if validation_error:
            return Response(
                {"error": validation_error},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            teacher = serializer.save()
            return Response(TeacherSerializer(teacher).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def validate_email(self, email_id):
        
        if Teacher.objects.filter(email_id=email_id).exists():
            return "A teacher with this email_id already exists in the database."
        return None


# Detail Views for Update and Delete
class StudentDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Student, pk=pk)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CourseDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Course, pk=pk)

    def put(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeacherDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Teacher, pk=pk)

    def put(self, request, pk):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        teacher = self.get_object(pk)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        return JsonResponse({'error': 'Invalid credentials'}, status=400)

class UserCheckView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return JsonResponse({'message': f'You are authenticated as {request.user.username}'})

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Student Management System")



class MarkEntryView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            teacher = Teacher.objects.get(user=request.user)
        except Teacher.DoesNotExist:
            return Response({"error": "Only teachers can add marks."}, status=status.HTTP_403_FORBIDDEN)

        data = request.data.copy()
        data['teacher'] = teacher.id  # Inject teacher ID

        serializer = MarkSerializer(data=data)
        if serializer.is_valid():
            course = serializer.validated_data['course']
            if course not in teacher.courses.all():
                return Response({"error": "You are not assigned to this course."}, status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttendanceEntryView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            teacher = Teacher.objects.get(user=request.user)
        except Teacher.DoesNotExist:
            return Response({"error": "Only teachers can add attendance."}, status=status.HTTP_403_FORBIDDEN)

        data = request.data.copy()
        data['teacher'] = teacher.id  # Inject teacher ID

        serializer = AttendanceSerializer(data=data)
        if serializer.is_valid():
            course = serializer.validated_data['course']
            if course not in teacher.courses.all():
                return Response({"error": "You are not assigned to this course."}, status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AllotCoursesToTeacherView(APIView):
    permission_classes = [IsAuthenticated]  # You can change this to [IsAdminUser] if needed

    def post(self, request):
        teacher_id = request.data.get('teacher_id')
        course_ids = request.data.get('course_ids')  # should be a list

        if not isinstance(course_ids, list):
            return Response({'error': 'course_ids must be a list.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return Response({'error': 'Teacher not found.'}, status=status.HTTP_404_NOT_FOUND)

        courses = Course.objects.filter(id__in=course_ids)

        if not courses.exists():
            return Response({'error': 'No valid courses found with given IDs.'}, status=status.HTTP_400_BAD_REQUEST)

        teacher.courses.set(courses)  # Overwrites previous assignments
        teacher.save()

        return Response({'message': 'Courses successfully allotted to teacher.'}, status=status.HTTP_200_OK)
