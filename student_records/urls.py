from django.urls import path
from .views import Student_Details
from .views import StudentDetailsPost,Course_Details,CoursetDetailsPost

urlpatterns = [
    path('student_details/', Student_Details),
    path('student_create/', StudentDetailsPost.as_view()),
    path('course_details/', Course_Details),
    path('course_create/', CoursetDetailsPost.as_view())
]
