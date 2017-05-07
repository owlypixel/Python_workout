Steps to generate a new website with Django
- django-admin startproject electronic_kit
- python manage.py migrate
- python manage.py runserver
- django-admin startapp products
- pip install django-debug-toolbar
- add debug_toolbar, products in INSTALLED APPS section
- add 'debug_toolbar.middleware.DebugToolbarMiddleware' to MIDDLEWARE
- add url settings
- add IP
- add .gitignore
_________________________
- create model
- python manage.py makemigrations
- python manage.py migrate
_________________________
- python manage.py shell
- create 2 products in shell
__________________________
- python manage.py createsuperuser
- pass electrokit
_________________________
- register Product in admin
_________________________
- change model (add category)
- apply migrations
- register category in admin.py
- create relationship between product and category in admin
_________________________
- add list catogories methods
- add class ProductAdmin to enhance admin area
- enhancing columns in the admin view for products
- sorting in columns
__________________________
- creating home url with products list
- rendering first template
-----------------------------------
Adding REST API
- pip install djangorestframework
- add framework in INSTALLED APPS settings
- make a serializer class for models (serializers.py)
- in views.py import all needed stuff and make a class-based view
- in app-level urls.py import stuff and add import it in the main urls.py