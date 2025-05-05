from rest_framework import serializers
from .models import Student, Course, Teacher

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'course_code']

class StudentSerializer(serializers.ModelSerializer):
    # Accept course IDs when creating/updating
    courses = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Course.objects.all(),
        write_only=True,
        required=False
    )

    # Show full course details when retrieving
    course_details = CourseSerializer(source='courses', many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'student_id', 'name', 'age', 'courses', 'course_details']


class TeacherSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Course.objects.all(),
        required=False
    )

    class Meta:
        model = Teacher
        fields = ['id', 'teacher_name', 'courses']
