# Web-Developement
![Alt Text](https://img.shields.io/badge/Python-3.7.4-red)
![Alt Text](https://img.shields.io/badge/django-3.0.8-blue)
![Alt Text](https://img.shields.io/badge/HTML-5-brightgreen)
![Alt Text](https://img.shields.io/badge/CSS-3-red)
![Alt Text](https://img.shields.io/badge/JavaScript-5.1-yellowgreen)
![Alt Text](https://img.shields.io/badge/Bootstap-3-green)
![Alt Text](https://img.shields.io/badge/jQuery-3.5.1-yellow)<br/>

**[MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)** 
**[CodePen](https://codepen.io/)**
**[Bootstrap](https://getbootstrap.com/docs/4.5/components/alerts/)**

* **Full stack Developement**
* Landing Page
* Calender
* Connect Four Game
* Image Slider
* Tansition Dropdown Menu
* CSS Timeline
* Pricing tables with Sass
* CSS Image Gallery
* Animated Car
* Animated Bootstrap Template
* Newsletter Design with LESS

## How to install django:
```bash
pip install django
```
Then
```bash
django-admin startproject projectName
```
Here you'll see bunch of files in the projectName folder:
* **\_\_init\_\_.py:** This is a blank Python script that due to its special name let’s Python know that this directory can be treated as a package
* **settings.py:** This is where you will store all your project settings
* **urls.py:** This is a Python script that will store all the URL patterns for your project. Basically the different pages of your web application.
* **wsgi.py:** This is a Python script that acts as the Web Server Gateway Interface. It will later on help us deploy our web app to production
* **manage.py:** This is a Python script that we will use a lot. It will be associates with many commands as we build our web app!


```bash
python manage.py runserver
```

This will give you an IP address of a server which will give you a notice that django is successfully working.
```bash
Django version 3.0.8, using settings 'first_project.settings'
Starting development server at http://127.0.0.1:8000/
```
You'll see some x number of warnings so, to remove the run the following command in CLI:
```bash
python manage.py migrate
```
This will migrate all the resources which are needed for this project.

For building you first django application:
```bash
python manage.py startapp firstApp
```
You'll get a folder by name firstApp:
* **\_\_init__.py:** This is a blank Python script that due to its special name let’s Python know that this directory can be treated as a package
* **admin.py:** You can register your models here which Django will then use them with Django’s admin interface.
* **apps.py:** Here you can place application specific configurations 
* **models.py:** Here you store the application’s data models 
* **tests.py:** Here you can store test functions to test your code
* **views.py:** This is where you have functions that handle requests and return responses
* **Migrations folder:** This directory stores database specific information as it relates to the models

