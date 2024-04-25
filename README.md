Project - a Python web application utilizing Django and Django Rest Framework, aimed at educational purposes. It encompasses three main applications:
testing_system: This application concentrates on all aspects related to courses, topics, tests,test access questions, answers, attempts,recommendations.
mentorship: This application covers all aspects related to users: teachers, students, groups, and regular users, also providing functionality for sending SMS.
chat: In this application, all aspects related to chat rooms and message exchange between students and teachers are implemented.

To run the project, follow these steps:
Make sure you have Docker and Docker Compose installed.
Clone the project repository by executing the following command:
bash
Copy code
git clone https://github.com/kozulinamary/eduplatform_3.git
Create a .env file in the project's root directory based on the provided .env.dev file, and fill in the required environment variables.
Build and start the Docker containers: docker-compose up -d --build 
Open the application in a web browser by navigating to http://localhost:8000.

Project Structure:
Dockerfile: Configuration for building the Docker image.
docker-compose.yml: Configuration for Docker Compose to manage the containers.
entrypoint.sh: Shell script to execute tasks when the container starts.
pyproject.toml: Poetry project configuration file.
README.md: This file provides information about the project.
eduplatform/: Django project directory.
eduplatform/: Main Django project settings.
chat/: Directory for chat functionality.
testing_system/: Directory for testing system functionality.
mentorship/: Directory for mentorship functionality.
This project uses PostgreSQL as the database backend. To configure PostgreSQL, ensure you have PostgreSQL installed on your system or use the provided Docker configuration.

Dependencies:

Python 3.11
Django 4.2.4
Django REST Framework 3.11.x
Python-dotenv 1.0.0
Psycopg2 2.9.9
Pillow 10.1.0
Mentorship 0.0.1
Channels 4.0.0
Channels-Redis 4.2.0
Development Dependencies:

Black 23.7.0
Isort 5.13.2
Flake8 7.0.0
To run tests, use the following command:

bash
Copy code
python manage.py test

We welcome contributions! Please feel free to open issues or submit pull requests.