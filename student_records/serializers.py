from rest_framework import serializers
from .models import Student, Course, Teacher, Mark,Attendance

# Serializer for Course model
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'course_code']

# Serializer for Student model (with roll_number instead of student_id)
class StudentSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Course.objects.all(),
        required=False
    )
    
    class Meta:
        model = Student
        fields = ['id', 'roll_number', 'name', 'age', 'courses'] 



# Serializer for Teacher model
class TeacherSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Course.objects.all(),
        required=False
    )

    class Meta:
        model = Teacher
        fields = ['id', 'teacher_name', 'email_id', 'courses']

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'