from rest_framework import serializers

from .models import Attendance, Classroom, Course, Mark, Student, Teacher


class StudentSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Course.objects.all(), required=False
    )
    classroom = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.all(), required=False
    )

    class Meta:
        model = Student
        fields = ["id", "roll_number", "name", "age", "courses", "classroom"]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "course_name", "course_code"]


class TeacherSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Course.objects.all(), required=False
    )

    class Meta:
        model = Teacher
        fields = ["id", "teacher_name", "email_id", "courses"]


class ClassroomSerializer(serializers.ModelSerializer):
    # Nested (for output)
    coordinator = TeacherSerializer(read_only=True)
    teachers = TeacherSerializer(many=True, read_only=True)
    students = StudentSerializer(many=True, read_only=True)

    # IDs for input
    coordinator_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), source="coordinator", write_only=True
    )
    teacher_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Teacher.objects.all(), source="teachers", write_only=True
    )
    student_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Student.objects.all(), source="students", write_only=True
    )

    class Meta:
        model = Classroom
        fields = [
            "id", "name",
            "coordinator", "coordinator_id",
            "teachers", "teacher_ids",
            "students", "student_ids"
        ]

    # Custom save logic for M2M fields
    def create(self, validated_data):
        teachers = validated_data.pop("teachers", [])
        students = validated_data.pop("students", [])
        classroom = Classroom.objects.create(**validated_data)
        classroom.teachers.set(teachers)
        classroom.students.set(students)
        return classroom

    def update(self, instance, validated_data):
        teachers = validated_data.pop("teachers", None)
        students = validated_data.pop("students", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if teachers is not None:
            instance.teachers.set(teachers)
        if students is not None:
            instance.students.set(students)

        return instance

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = "__all__"


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"
