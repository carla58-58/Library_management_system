Library Management System App


📋 Table of Contents

1. 🤖 [Introduction](#introduction)
2. ⚙️ [Tech Stack](#tech-stack)
3. 🔋 [Features](#features)
4. 🤸 [Quick Start](#quick-start)


🤖 Introduction

Welcome to the Django Library Management System App! This web application is designed to simplify and digitize the management of library resources, providing an intuitive interface for librarians and users alike.

Built with Django and SQLite, the app enables users to manage books, members, and lending activities efficiently, making it ideal for schools, colleges, and small to medium-sized libraries


⚙️ Tech Stack

- Django – High-level Python web framework for rapid development and clean, pragmatic design

- Python – Main programming language powering the backend logic

- SQLite – Lightweight, file-based database for easy setup and local development

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

   *Run the development server into Library_management_system\pythonProject1\mysite directory:
   python manage.py runserver

Open [http://localhost:8000] in your browser to view the app.

Thank you for checking out the Django Library Management System App! If you’d like to collaborate or learn more, please don’t hesitate to reach out
