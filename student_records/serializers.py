from rest_framework import serializers
from .models import Student, Course, Teacher

# Serializer for Course model
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'course_code']

# Serializer for Student model
class StudentSerializer(serializers.ModelSerializer):
    # The 'courses' field represents a many-to-many relationship to the Course model

    courses = serializers.PrimaryKeyRelatedField(
        many=True,  # This means that a student can have multiple courses (many-to-many relationship)
        queryset=Course.objects.all(), 
        required=False
    )

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'email', 'courses']

# Serializer for Teacher model
class TeacherSerializer(serializers.ModelSerializer):
    # The 'courses' field represents a many-to-many relationship to the Course model
    courses = serializers.PrimaryKeyRelatedField(
        many=True, # This means that a teacher can teach multiple courses (many-to-many relationship)
        queryset=Course.objects.all(),
        required=False
    )

    class Meta:
        model = Teacher  # Specifies that this serializer is for the 'Teacher' model
        fields = ['id', 'teacher_name', 'courses'] # Fields from the 'Teacher' model to include in the serialized output
