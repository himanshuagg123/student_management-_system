from django.urls import path
from .views import StudentListView, CourseListView, TeacherListView, CourseDetailView, StudentDetailView, TeacherDetailView

urlpatterns = [
    # List views
    path('students/', StudentListView.as_view()),  # List of all students
    path('courses/', CourseListView.as_view()),  # List of all courses
    path('teachers/', TeacherListView.as_view()),  # List of all teachers
    
    # Detail views
    path('courses/<int:pk>/', CourseDetailView.as_view()),  
    path('students/<int:pk>/', StudentDetailView.as_view()),  
    path('teachers/<int:pk>/', TeacherDetailView.as_view()),  
]
