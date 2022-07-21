# SupplyerManagementSystem

## Introduction
This is an Supplyer Management System Which helps Supplyer to make note of everything which they supplies to Their Coustomer's We build Backend in DJango and React as FrontEnd and we used django backed as an API in React App. This Project Consist of Admin Panel Where admin can handle all the Worker data and their activities, Also Admin can also manage products data and managing them accordingly.

## BackEnd Installation
* Creating an Virtual Environment
```
python3 -m venv venv
```
```
python3 -m venv venv
```
```
source venv/bin/activate
```
* Packeges Which Are Required 
```
pip install django djangorestframework django-cors-headers djangorestframework-simplejwt Pillow psycopg2-binary 
```
* Database Migrations
```
python manage.py makemigrations
python manage.py migrate
```
* Creating Super User
```
python manage.py createsuperuser
```
* Start Server 
```
python manage.py runserver
```
## ReactAPP Configuration
* Creation of an react app
```
npx create-react-app (Project Name)
```
