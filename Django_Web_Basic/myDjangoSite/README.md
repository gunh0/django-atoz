```powershell
> pip install virtualenv
> virtualenv venv		// virtualenv 'name'
> .\venv\Scripts\activate.ps1
> deactivate
```

```shell
$ find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
$ find . -path "*/migrations/*.pyc" -delete

python manage.py makemigrations
python manage.py migrate
python .\manage.py createsuperuser

python manage.py runserver
```

