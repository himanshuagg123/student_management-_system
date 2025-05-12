from django.urls import path
from .views import StudentListView, CourseListView, TeacherListView, CourseDetailView, StudentDetailView, TeacherDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # JWT Authentication URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # List views
    path('students/', StudentListView.as_view()),  # List of all students
    path('courses/', CourseListView.as_view()),  # List of all courses
    path('teachers/', TeacherListView.as_view()),  # List of all teachers
    
    # Detail views
    path('courses/<int:pk>/', CourseDetailView.as_view()),  
    path('students/<int:pk>/', StudentDetailView.as_view()),  
    path('teachers/<int:pk>/', TeacherDetailView.as_view()),  
]
