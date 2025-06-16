# 🎓 Student Management System (Backend API)

A complete backend system built with Django and Django REST Framework that allows educational institutions to manage students, teachers, courses, attendance, and marks securely and efficiently.

---

## 🚀 Project Overview

The Student Management System helps schools or colleges automate the following tasks:

- 📋 Register and manage students
- 📘 Add and organize courses
- 👨‍🏫 Create teachers and assign them to specific courses
- 📝 Allow teachers to record marks for students only in the subjects they teach
- 📅 Let teachers mark attendance per course
- 🔐 Authenticate users and restrict sensitive operations to only authorized teachers

This project mimics a real-world multi-role academic environment, applying proper data validation and access control.

---

## 💡 Why I Built This Project

I built this project to:

- Understand how to design relationships between real-world entities like students, teachers, and courses.
- Practice implementing authentication, role-based permissions, and data validation in a Django REST API.
- Learn Django ORM and use it to create clean, efficient, and secure APIs.
- Simulate a real-life academic system as found in schools, colleges, or coaching platforms.

---

## 🛠️ Tech Stack

| Layer            | Technology                      |
|------------------|----------------------------------|
| Backend          | Django, Django REST Framework   |
| Authentication   | Django built-in auth system     |
| Database         | SQLite (can be upgraded to PostgreSQL) |
| API Testing      | Postman / Swagger UI            |
| Version Control  | Git & GitHub                    |
| Tools            | VSCode, Django Admin            |

---

## 🧩 Features

### 👨‍🎓 Students
- Add new students with unique roll numbers
- Update or delete existing student records
- Assign students to multiple courses

### 📘 Courses
- Add new courses with a unique course code
- Update/delete courses

### 👨‍🏫 Teachers
- Create teachers with unique email IDs
- Assign them to specific courses
- Only the assigned teachers can:
  - Add marks for students in their courses
  - Record attendance

### 📝 Marks
- Only the teacher who teaches a course can give marks to students in that course
- Stores student, course, teacher, marks, and date

### 📅 Attendance
- Teachers mark whether a student was present or absent for a course on a specific date
- Role-checked to avoid unauthorized access

### 🔐 Authentication
- Login API using Django’s authentication system
- Access to sensitive views restricted to authenticated users (teachers)

---

## 🔗 Data Relationships

- A **Student** can take many **Courses** (ManyToMany)
- A **Teacher** can teach many **Courses** (ManyToMany)
- **Marks** and **Attendance** records link:
  - 1 student 🔗 1 course 🔗 1 teacher
### ⚙️ Setup Instructions

**1. Clone the repository**
```bash
git clone https://github.com/your-username/student-management-system.git
cd student-management-system
```

**2. Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**5. Create a superuser (admin)**
```bash
python manage.py createsuperuser
```

**6. Run the server**
```bash
python manage.py runserver
```



### 🔄 Sample API Endpoints

| Endpoint            | Method | Description                                   |
|---------------------|--------|-----------------------------------------------|
| `/api/students/`    | GET    | List all students                             |
| `/api/students/`    | POST   | Add a new student                             |
| `/api/courses/`     | GET    | List all courses                              |
| `/api/courses/`     | POST   | Add a new course                              |
| `/api/teachers/`    | GET    | List all teachers                             |
| `/api/teachers/`    | POST   | Add a new teacher                             |
| `/api/marks/`       | POST   | Add marks (only by the assigned teacher)      |
| `/api/attendance/`  | POST   | Mark attendance (only by the assigned teacher)|
| `/api/login/`       | POST   | User login                                    |
| `/api/check-auth/`  | GET    | Check that the user is authenticated          |

🧠 Skills Demonstrated
Django REST Framework fundamentals

Role-based access control

Object-relational mapping (ORM)

RESTful API design

Secure and modular backend development

Real-world relationships and permissions (Student–Course–Teacher)

API authentication and session handling

📸 Future Improvements
Add Swagger/OpenAPI documentation

Add student dashboard views

Implement JWT authentication

Export marks and attendance to Excel/PDF

Frontend using React or Next.js

🙋‍♂️ Author
Himanshu Aggarwal
