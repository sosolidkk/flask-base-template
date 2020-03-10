# Stuff

### Index page
- navbar
    - item-1
    - item-2
    - item-3
    - Login
        - login-form
    - registration
- image-slider
- jumbotron-1
- jumbotron-2
- jumbotron-2

### Logged in page
- dashboard
- sidebar

### Registration
- registration-form

### Libraries
- Flask
- Flask-SQLAchemy
- Flask-Login
- Flask-Migrate
- Flask-WTF

### App file structure
```
|-- app/
|   |-- web/
|   |   |-- static/
|   |   |   |-- css/
|   |   |   |-- images/
|   |   |   |-- js/
|   |   |-- templates/
|   |   |   |-- base.html
|   |   |   |-- index.html (also login)
|   |   |   |-- dashboard.html
|   |   |   |-- registration.html
|   |-- __init__.py
|   |-- routes.py
|   |-- models.py
|   |-- form.py
|-- .gitignore
|-- base.py
|-- config.py
|-- LICENSE
|-- README-en.md
|-- README.md
|-- requirements.txt
|-- todo.md
```