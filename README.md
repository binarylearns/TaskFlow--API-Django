# TaskFlow REST API

A RESTful Task Management API built using **Django** and **Django REST Framework**. This project aims to demonstrate backend development skills, including CRUD operations, user authentication, permissions, data validation, filtering, and API testing.

## 🚀 Project Overview

TaskFlow is a backend API designed to help users manage their daily tasks. Users will be able to create, retrieve, update, and delete tasks, organize them into categories, and manage task priorities and deadlines.

## 🛠️ Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- Git & GitHub

## ✨ Planned Features

- User registration and authentication
- Task creation, retrieval, updating, and deletion (CRUD)
- Category management
- Task priority and status management
- User-specific task permissions
- Search and filtering
- Pagination
- API documentation (Swagger/OpenAPI)
- Unit testing

## 📂 Project Structure

```text
TaskFlow-REST-API/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── tasks/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── ...
│
├── manage.py
└── README.md
```

## ⚙️ Installation and Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd TaskFlow-REST-API
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

**Linux/macOS:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install django djangorestframework
```

5. Apply database migrations:

```bash
python manage.py migrate
```

6. Start the development server:

```bash
python manage.py runserver
```

## 📌 Development Progress

- [x] Phase 1: Project setup and environment configuration
- [x] Phase 2: Database models and serializers 
- [x] Phase 3: Task and category CRUD operations 
- [x] Phase 4: Authentication and permissions 
- [x] Phase 5: Filtering, searching, and pagination 
- [x] Phase 6: Unit testing [Working on this]
- [ ] Phase 7: API documentation and final improvements

## 🎯 Project Objective

The main objective of this project is to strengthen practical knowledge of REST API development using Django REST Framework while following proper backend development practices.

## 📖 Project Status

**Currently in development –  Phase 6: Unit testing [Working on this]**

More features and improvements will be added as development progresses.

## 👨‍💻 Author

BinaryLearns
