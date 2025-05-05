from django.urls import path
from .views import StudentListView, CourseListView, TeacherListView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student-list'),     # Handles GET + POST
    path('courses/', CourseListView.as_view(), name='course-list'),        # Handles GET + POST
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),     # Handles GET + POST
]
