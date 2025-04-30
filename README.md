# Student Management System

A basic Student Management System built using **Django** and **Django Rest Framework (DRF)**. This project demonstrates creating and managing APIs using both Function-Based Views (FBV) and Class-Based Views (CBV).

---

## 📅 Day 1 Progress

### ✅ Project Setup
- Created a Django project named **Student Management System**.
- Created an app called `student_records`.

### 📦 Student Model
Defined a `Student` model with the following fields:
- `name` (type: `CharField`)
- `age` (type: `IntegerField`)
- `email` (type: `EmailField`)

### 🔧 APIs for Student
Created two APIs to handle student data:

1. **Function-Based View**:  
   `Student_details` – Fetches the list of students via GET request.

2. **Class-Based View**:  
   `StudentDetailsPost` – Allows posting student data to the database via POST request.

### 🌐 URL Routing
- Configured `urls.py` to route to both APIs.

### 🧪 Testing APIs with Postman
- **GET Request**: Fetch student list using `Student_details` endpoint.
- **POST Request**: Submit student data in JSON format using the raw body in Postman to the `StudentDetailsPost` endpoint.

---

## 📚 Learning Note

### 🔄 Serializers in DRF
Initially, data was manually returned in JSON format. Later, DRF **serializers** were implemented for cleaner and more maintainable code.

**Serializer Functionality:**
- Convert complex data types like Django models into native Python datatypes.
- Easily render output into JSON.
- Validate incoming data.
- Deserialize JSON into Django model instances.

---

## 📘 Course Model

### 🛠️ Course Model Fields:
- `course_name` (type: `CharField`)
- `course_code` (type: `CharField`)

### 🔧 APIs for Course
Created two APIs similar to the student model:

1. **Function-Based View**:  
   `course_Details` – Fetches the list of courses.

2. **Class-Based View**:  
   `CourseDetailsPost` – Allows posting course data to the database.

---

## 🛠️ Tools & Technologies
- Python 3.12
- Django 5.2
- Django REST Framework
- Postman (for API testing)

---
