from django.urls import path
from .views import Student_Details
from .views import StudentDetailsPost

urlpatterns = [
    path('student_details/', Student_Details),
    path('student_create/', StudentDetailsPost.as_view())
]
