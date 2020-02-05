##### Required:
* python 3.8
* django 3.0
* django rest framework 3.11
* djangorestframework-jwt 1.11
* djangorestframework-simplejwt 4.4
* django-likes 2.0

##### Optional:
* virtual env

##### Installation process:
* Clone repository: **git clone https://github.com/adrianashymoniak/starnavi_test_task.git**
* Create virtual env:  run command in terminal **python -m venv myvenv**
* Activate virtual env (optional): **source myvenv/bin/activate**
* run: **pip install -r requirements.txt** (for installing required libraries in your virtual env)
* Make sure your virtual environment is activated and requirements are installed    
* Go to **social_network** folder and run migration: **python manage.py migrate**
* Run server locally: **python manage.py runserver**
* Open browser and go to  **http://127.0.0.1:8000/** -> click login or go to **http://127.0.0.1:8000/auth/register** to create your own user

