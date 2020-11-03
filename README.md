# Django

Django is a high-level Python web framework that enables rapid development of secure and maintainable web applications. It follows the Model-View-Controller (MVC) architectural pattern, which separates the application logic into three interconnected components - models (database), views (user interface), and controllers (business logic).

<br/>

### MVC (Model-View-Controller)

MVC stands for Model-View-Controller, which is a software design pattern used to separate an application's data (Model), user interface (View), and control flow (Controller) into three interconnected components. The main idea behind the MVC pattern is to provide a clear separation of concerns, so that each component can be developed, tested, and maintained independently.

Here's a brief overview of each component:

-   Model: The Model component represents the data and business logic of the application. It interacts with the database or any other data source to perform CRUD (Create, Read, Update, Delete) operations on the data.

-   View: The View component represents the user interface of the application. It displays the data to the user and handles user input, such as button clicks or form submissions.

-   Controller: The Controller component acts as the intermediary between the Model and the View. It receives input from the user via the View, processes it using the Model, and updates the View accordingly.

By separating the concerns of an application into these three components, the MVC pattern makes it easier to develop, test, and maintain the code. For example, changes to the user interface can be made without affecting the underlying data or business logic, and changes to the data can be made without affecting the user interface.

<br/>

### Model-View-Template (MVT)

In Django, the Model-View-Template (MVT) pattern is used instead of the traditional Model-View-Controller (MVC) pattern. The MVT pattern is very similar to the MVC pattern, but with some differences in the terminology and responsibilities of the components.

In summary, the main difference between MVT and MVC is that the MVT pattern separates the responsibilities of the Controller into two components: the View and the Template. The View handles the business logic, while the Template handles the presentation logic.

> -   Implement Project Body
> -   Model (models.py, admin.py)
> -   URLconf (urls.py)
> -   Views (views.py)
> -   Templates (templates/)

<br/>

When deploying a Django application in a production environment, a web server such as Apache or nginx is required to handle the incoming requests from multiple users. The web server communicates with the WSGI (Web Server Gateway Interface) which in turn communicates with the Django application to handle the requests and return responses to the users.

When running the Django development server using `python manage.py runserver`, it provides a simple web server for testing and development purposes only, and should not be used in a production environment.

![image](https://user-images.githubusercontent.com/41619898/81892420-0fe67680-95e6-11ea-8188-d2ec81d1411e.png)

<br/>

#### settings.py

- settings.py is the configuration file for a Django project, and when a new project is created, Django automatically registers some default settings.
- By default, Django uses the SQLite3 database engine.
- The file contains settings related to various directories, logging formats, debugging mode, security, and other project-specific aspects.

<br/>

#### models.py

- models.py is where tables are defined in Django and it uses the Object-Relational Mapping (ORM) technique for database processing.
- In other words, the tables are mapped to classes so that the Create, Read, Update, Delete (CRUD) functions are performed on the class objects, and Django internally reflects these changes on the database.
- In Django, tables are defined as a single class and the columns of the table are mapped to variables (attributes) of the class.
  When changes to the database occur in the models.py file, such as creating a new table or modifying the definition of an existing one, it is necessary to perform a migration to reflect the changes in the database.

<br/>

#### Migrations

- Migrations are records of changes to the database, including creation, deletion, and modification of tables and fields.
- Physically, migration files exist under the `migrations/` directory of each application in the project.

<br/>

#### URLconf

- URLconf refers to the `urls.py` file, which maps URLs to views (functions or methods).
- When defining URLconf, you can define it in a single file or split it into two files, project URL and app URL, for ease of extension and modification.

<br/>

#### views.py

- `views.py` is the most important file where view logic is coded. As the scope of the project grows, the logic also becomes more complex, and the coding volume of `views.py` also increases. Therefore, it is important to consider readability, maintainability, and reusability.
- Views can be coded as functions or classes, which are referred to as Function-based views and Class-based views, respectively.

<br/>

#### Templates

- In web programming, a template file (*.html) is required for each web page. Therefore, when developing web applications, several template files are created, and a template directory is required to store these files.
- Template directories are divided into project template directories and app template directories.
- The project template directory is a directory specified in the DIRS field of the TEMPLATES setting.
- The app template directory refers to the templates/ directory that exists in each application directory.
- The project template directory stores files related to the overall look and feel of the entire project, such as base.html. Template files used by each app are located in the app template directory.

<br/>

#### Admin

- The Admin provides a function to view and modify the contents of a table.
- The Admin site provides functionality to prepare this content, which is referred to as "content."
- In the Admin site, you can perform operations such as inputting, modifying, and deleting data for tables, including the User and Group tables.

<br/>

#### runserver

- It is a test web server that runs and tests the code written during development.

<br/>

### Advantages of Django

-   **Object-Relational Mapping (ORM) Support** − Django provides a bridge between the data model and the database engine, and supports a large set of database systems including MySQL, Oracle, Postgres, etc. Django also supports NoSQL database through Django-nonrel fork. For now, the only NoSQL databases supported are MongoDB and google app engine.
-   **Multilingual Support** − Django supports multilingual websites through its built-in internationalization system. So you can develop your website, which would support multiple languages.
-   **Framework Support** − Django has built-in support for Ajax, RSS, Caching and various other frameworks.
-   **Administration GUI** − Django provides a nice ready-to-use user interface for administrative activities.
-   **Development Environment** − Django comes with a lightweight web server to facilitate end-to-end application development and testing.

<br/>

### Basic Running Command / Reset Migrations

```shell
# Windows
pip install virtualenv
virtualenv venv  // virtualenv 'name'
.\venv\Scripts\activate.ps1
deactivate   // virtualenv exit
```

```shell
# Using Anaconda
conda create -n django_311 python=3.11.0
activate venv

# virtual env. deactivate
deactivate

# delete env.
conda env remove -n venv
```

```shell
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# Username (leave blank to use ''): root
# Email address: test@test.com
# Password: 1234
# Password (again): 1234

python manage.py runserver
# Django version 4.1.7, using settings 'mysite.settings'
# Starting development server at http://127.0.0.1:8000/
```
