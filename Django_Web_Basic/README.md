## Start Project

```bash
python --version
Python 3.5.6 :: Anaconda, Inc.

# make python 3.5 env.
conda create -n django35 python=3.5

# check Django version
pip list | grep Django
Django     2.0
```

```powershell
> pip install virtualenv
> virtualenv venv		// virtualenv 'name'
> .\venv\Scripts\Activate
(venv) myDjangoSite> python -m pip install -r requirements.txt

// Check Username/Password & Change Password by shell
> python manage.py shell
> from django.contrib.auth.models import User
> User.objects.filter(is_superuser=True)
> super_id = User.objects.get(username='admin')
> super_id.set_password('1234')
> super_id.save()

// Initializing DB
$ find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
$ find . -path "*/migrations/*.pyc" -delete
$ rm db.sqlite3

myDjangoSite> python manage.py makemigrations
myDjangoSite> python manage.py migrate
myDjangoSite> python manage.py createsuperuser
myDjangoSite> python manage.py runserver
```

<br/>

### 0 Admin

-   **http://localhost:8000/admin/**

### #1 Blog App

-   **http://localhost:8000/blog/**

### #2 Bookmark App

-   **http://localhost:8000/bookmark/**
