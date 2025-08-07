Library Management System App


📋 Table of Contents

1. 🤖 [Introduction](#introduction)
2. ⚙️ [Tech Stack](#tech-stack)
3. 🔋 [Features](#features)
4. 🤸 [Quick Start](#quick-start)


🤖 Introduction

Welcome to the Django Library Management System App! This web application is designed to simplify 
and digitize the management of library resources, providing an intuitive interface for librarians 
and users alike.


Built with Django, the app enables users to manage books, members, and lending activities efficiently, 
making it ideal for schools, colleges, and small to medium-sized libraries.

For local development, the app uses SQLite for easy setup. 
For cloud deployment on AWS, it uses PostgreSQL (via Amazon RDS) for robust, scalable, 
and secure data storage.


⚙️ Tech Stack

- Django – High-level Python web framework for rapid development and clean, pragmatic design

- Python – Main programming language powering the backend logic

- SQLite – Lightweight, file-based database for easy setup and local development (used locally)
- PostgreSQL (AWS RDS) – Managed, scalable database for production deployment on AWS

- HTML/CSS & Bootstrap – For responsive and user-friendly web interfaces

- Django Auth – Built-in authentication system for secure user and admin access


🔋 Features

👉 **Book Management**: Add, update, delete, and view books with details like title, author, genre, and availability

👉 **Member Management**: Register, update, and delete member records; manage student or user profiles

👉 **Lending System**: Issue and return books, track due dates

👉 **Search & Filter**: Search books by title, author, or genre for quick access

👉 **Admin Dashboard**: Centralized dashboard for managing books, members, and lending records

👉 **User Authentication**: Secure login/signup for both admins and users

👉 **Borrowing History*: View borrowing logs and member activity

👉 **Responsive Design*: Optimized for desktops, tablets, and mobile devices


🤸 Quick Start

Ready to run the app locally or explore the code? Here’s how you can get started:

-Prerequisites:
   Python 3.x
   Django
   Git

-Installation:

   *Clone the repository:
   git clone <repository-url>
   
   *Create a virtual environment and activate it:
   python3 -m venv env
   source env/bin/activate # On Windows: env\Scripts\activate
   
   *Install dependencies:
   pip install -r requirements.txt
   
   *Apply migrations to set up the database:
   python manage.py migrate
   
   *Create a superuser for admin access:
   python manage.py createsuperuser

-Running the Project:

   *Run the development server (cd Library_management_system\pythonProject1\mysite directory):
   python manage.py runserver


🌩️ AWS Deployment

This application is deployed on Amazon Web Services (AWS) to provide a scalable, reliable, 
and cloud-based solution for library management. The deployment uses two main AWS services:

- **EC2 (Elastic Compute Cloud):** A virtual server that hosts the Django application. 
The app runs inside a Docker container, which makes it easy to manage dependencies and deployment.
- **RDS PostgreSQL (Relational Database Service):** A managed PostgreSQL database that stores all 
application data, such as books, users, and lending records. RDS handles backups, scaling, and maintenance automatically.

**Deployment Architecture:**
- The EC2 instance runs the Django app and communicates with the RDS PostgreSQL database over a private network connection.
- Environment variables (such as database credentials and host) are stored in a `.env` file on the EC2 instance and loaded by the Django app.
- Security groups are configured so that only the EC2 instance can access the RDS database, improving security.

**Deployment Process:**
1. The source code is cloned onto the EC2 instance.
2. Docker and Docker Compose are installed to build and run the Django app in a container.
3. The `.env` file is created with the RDS database connection details.
4. The app is started using Docker Compose, which builds the container and launches the web server.
5. Database migrations are applied, and an admin user is created for management access.

**Benefits of AWS Deployment:**
- The app is accessible from anywhere, not just locally.
- AWS provides automatic backups, scaling, and high availability for the database.
- Using Docker ensures consistent environments and easy updates.
- Security groups and managed services help protect your data and infrastructure.

This setup allows the Library Management System to serve multiple users and scale as needed, 
while keeping data secure and operations reliable.

Open [http://44.202.167.102:8000/] in your browser to view the app.

Thank you for checking out the Django Library Management System App! If you’d like to collaborate or learn more, please don’t hesitate to reach out
