# Blogging Platform API

A **RESTful API** built with **Django & Django REST Framework** for managing blogs, users, and authentication. This project serves as a backend for a blogging platform and demonstrates CRUD operations, role-based permissions, JWT authentication, filtering, and Docker deployment.

---

## Table of Contents

- [Features](#features)  
- [Technologies](#technologies)  
- [Getting Started](#getting-started)  
- [Environment Variables](#environment-variables)  
- [Database](#database)  
- [Docker Setup](#docker-setup)  
- [API Endpoints](#api-endpoints)  
- [Testing](#testing)  
- [Deployment](#deployment)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Features

- User registration and JWT authentication  
- Role-based access control: Admin, Staff, Regular User  
- Create, read, update, delete (CRUD) blog posts  
- Manage categories and tags (admin only)  
- Filter posts by author, category, or tags  
- Commenting and like/dislike functionality (planned)  
- Dockerized for consistent development and deployment  
- Swagger/OpenAPI documentation (planned)  

---

## Technologies

- **Python 3.12**  
- **Django 5.2.5**  
- **Django REST Framework**  
- **djangorestframework-simplejwt** for JWT authentication  
- **MySQL 8.0**  
- **Docker & Docker Compose**  
- **Postman** for API testing  

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/awolcoder/Blogging-Platform-Api.git
cd Blogging-Platform-Api
