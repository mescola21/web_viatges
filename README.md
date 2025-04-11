# 🌍 Web Viatges — Django Project

This project is a web platform built with **Django** as part of the Web Development course module. Its purpose is to serve as the foundation for a travel agency website, with user management and static resources.

---

## 🧱 Project Structure

```bash
web_viatges/
├── .idea/                  # PyCharm configuration files
├── accounts/               # Main app (users, views, templates)
│   ├── migrations/
│   ├── templates/
│   └── __pycache__/
├── DjangoProject/          # Main Django project settings
│   └── __pycache__/
└── static/                 # Static resources (CSS, images)
    ├── css/
    └── images/

    
-Installation & Setup Prerequisites
    Make sure you have the following installed:

    Docker (for running the application in a containerized environment)

    Poetry (for managing dependencies)

-Step-by-Step Setup

    Clone the Repository:
    
        git clone https://github.com/mescola21/web_viatges/tree/miquel
        cd web_viatges
    
    From the project root directory, build the Docker image using docker-compose:
    
        docker-compose build
        
    Once the image is built, you can start the application:
    
        docker-compose up
    
    Open your browser and go to http://127.0.0.1:8000/ to see the project running.

    Usage:
    
        User Registration: You can sign up for a new account on the platform.
        
        User Login: Log in using your credentials.
        
        Explore Static Pages: The website contains several static pages such as images and custom CSS styles.
        
        Manage Profile: Once logged in, users can manage their profiles and settings.
        
        Other features: User can explore trips around the world and book them.

-Used technologies:

    Backend - Django (Python)
    Frontend - HTML5, CSS3, Boostrap
    Database - SQLite (default)
    DevOps - Docker, Docker-Compose
    Package Mgmt. - Poetry

-Project Goals:

    This project serves as a practice application for learning Django and web development, showcasing skills in user management, static files handling, and creating a functional web platform.
    
