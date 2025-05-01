# 🎓 Student Management System

A basic Student Management System built using **Django** and **Django Rest Framework (DRF)**.

---

## 📅 Day 1 Progress

### ✅ Project Setup
- Created a Django project named **Student Management System**
- Created an app called `student_records`

---

## 🧑‍🎓 Student Model

### Fields:
- `name` (`CharField`)
- `age` (`IntegerField`)
- `email` (`EmailField`)
- `courses` (`ManyToManyField` to Course)

> Each student can enroll in multiple courses using the course ID and course name.

### APIs:
- **GET**: `Student_details` – Fetch list of students
- **POST**: `StudentDetailsPost` – Add new student with enrolled courses

---

## 📘 Course Model

### Fields:
- `course_name` (`CharField`)
- `course_code` (`CharField`)

> Courses can be assigned to both students and teachers using many-to-many relationships.

### APIs:
- **GET**: `course_Details` – Fetch list of courses
- **POST**: `CourseDetailsPost` – Add new course to the system

---

## 👨‍🏫 Teacher Model

### Fields:
- `name` (`CharField`)
- `courses` (`ManyToManyField` to Course)

> Each teacher can be assigned multiple courses.

### APIs:
- **GET**: Retrieve list of teachers and their assigned courses
- **POST**: Add a new teacher and assign courses

---

## 🌐 URL Routing
All APIs are properly routed through `urls.py` including:
- Student API routes
- Course API routes
- Teacher API routes

---

## 🧪 API Testing (Postman)
- **GET Requests**: 
  - Fetch all students, courses, and teachers
- **POST Requests**: 
  - Submit JSON data for students and teachers
  - Assign courses using course IDs

---

## 📚 Learning Note: DRF Serializers

Initially, JSON was manually returned. Later, DRF serializers were introduced for cleaner code and better abstraction.

### Serializer Benefits:
- Convert model instances to Python datatypes
- Render data into JSON
- Validate incoming request data
- Deserialize JSON into model instances

---

## 🛠️ Tools & Technologies
- Python 3.12
- Django 5.2
- Django REST Framework
- Postman (for API testing)

---

> Stay tuned for more features like attendance tracking, marks management, and admin controls!
