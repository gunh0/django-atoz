# Django

장고는 파이썬으로 작성된 오픈 소스 웹 애플리케이션 프레임워크이다.

그리고 대부분의 현대적 프레임워크와 마찬가지로, 장고는 MVC 패턴을 지원한다.

<br/>

### MVC (Model-View-Controller)

UI(웹 또는 데스크톱)를 제공하는 애플리케이션에 대해 이야기할 때는 대개 MVC 아키텍처에 대해 이야기한다.

그리고 이름에서 알 수 있듯이 MVC 패턴은 Model-View-Controller 세 가지 요소를 기반으로 한다.

<br/>

### MTV (Model-Templat-View)

MVT(Model-View-Template)는 MVC와 약간 다르다.

실제로 두 패턴의 주요 차이점은 Django 자체가 컨트롤러 부분(모델과 뷰의 상호작용을 제어하는 소프트웨어 코드)을 관리한다는 점이다.

여기서, 템플릿은 DTL(Django Template Language)과 혼합된 HTML 파일이다.

> - Implement Project Body
> - Model (models.py, admin.py)
> - URLconf (urls.py)
> - Views (views.py)
> - Templates (templates/)
>

<br/>

장고는 ‘웹 프레임워크’이며, 하나의 ‘애플리케이션’이다.

여러 사용자가 동시에 사이트에 접근할 경우, 이것을 처리하는 것은 ‘웹 서버’의 역할이다.

즉, python manage.py runserver 를 하면 웹 서버를 띄우기는 하지만,

단지 개발 테스트 용도로 제공해주는 것이다.

실제 배포할 경우에는 nginx 나 apache 같은 웹 서버가 필요하며,

웹 서버와 Python 애플리케이션인 장고가 통신할 수 있게 하는 WSGI(gunicorn, uwsgi 등)가 필요하다.

![image](https://user-images.githubusercontent.com/41619898/81892420-0fe67680-95e6-11ea-8188-d2ec81d1411e.png)

<br/>

> ### settings.py
>
> - 프로젝트 설정 파일로서 처음 프로젝트를 생성하면 장고가 기본 사항들을 자동으로 등록해준다.
> - 장고는 디폴트로 SQLite3 데이터베이스 엔진을 사용하는 것으로 지정한다.
> - 베이스(루트) 디렉터리를 포함한 각종 디렉터리의 위치, 로그의 형식, 디버그 모드, 보안 관련 사항 등 프로젝트의 전반적인 사항들을 설정한다.
>
> ---
>
> ### models.py
>
> - models.py는 테이블을 정의하는데 장고의 특징 중 하나로, 데이터베이스 처리는 ORM(Object Relation Mapping) 기법을 사용한다.
>
> - 즉, 테이블을 클래스로 매핑해서 테이블에 대한 CRUD(Create, Read, Update, Delete) 기능을 클래스 객체에 대해 수행하면, 장고가 내부적으로 데이터베이스에 반영해주는 방식이다.
>
> - 장고에서는 ORM 기법에 따라 테이블을 하나의 클래스로 정의하고, 테이블의 컬럼은 클래스의 변수(속성)로 매핑한다.
>
> - 테이블의 신규 생성, 테이블의 정의 변경 등 models.py 파일에서 데이터베이스 변경 사항이 발생하면, 이를 데이터베이스에 실제로 반영해주는 작업을 해야 한다.
>
> > ###### Migrations (마이그레이션)
>   >
> > - 테이블 및 필드의 생성, 삭제, 변경 등과 같이 데이터베이스에 대한 변경 사항을 알려주는 정보
>   >
> > - 물리적으로는 애플리케이션 디렉터리별로 migrations/ 디렉터리 하위에 마이그레이션 파일들이 존재
>
> ---
>
> ### URLconf
>
> - URL과 뷰(함수 또는 메소드)를 매핑해주는 urls.py 파일을 말한다.
> - URLconf를 정의할 때는 하나의 파일에 정의할 수도 있고, 2개의 파일에 정의할 수도 있는데 프로젝트 전체 URL을 정의하는 프로젝트 URL과 앱마다 정의하는 앱 URL, 2계층으로 나눠서 구현하는 것이 변경도 쉽고 확장도 용이하다.
>
> ---
>
> ### views.py
>
> - 뷰 로직을 코딩하는 가장 중요한 파일로서 프로젝트의 개발 범위가 커짐에 따라 로직도 점점 복잡해지고 views.py 파일의 코딩량도 많아지기 때문에 가독성과 유지보수 편리, 재활용 등을 고려해야 한다는 점이 중요하다.
> - 뷰 로직을 함수로 코딩할 것인지 클래스로 코딩할 것인지에 따라 Function-based view(함수형 뷰)와 Class-based view(클래스형 뷰)로 구분한다.
>
> ---
>
> ### templates
>
> - 웹 화면(페이지)별로 템플릿 파일(*.html)이 하나씩 필요하므로, 웹 프로그래밍 개발 시 여러개의 템플릿 파일을 작성하게 되고, 이런 템플릿 파일들을 한곳에 모아두기 위한 템플릿 디렉터리가 필요하다.
> - 템플릿 디렉터리는 프로젝트 템플릿 디렉터리와 앱 템플릿 디렉터리로 구분해서 사용한다.
> - 프로젝트 템플릿 디렉터리는 TEMPLATES 설정의 DIRS 항목에 지정된 디럭터리이다.
> - 앱 템플릿 디렉터리는 각 애플리케이션 디렉터리마다 존재하는 templates/ 디렉터리를 의미한다.
> - 프로젝트 템플릿 디렉터리에는 base.html 등 전체 프로젝트의 룩앤필(Look and feel)에 관련된 파일들을 모아두고, 각 앱에서 사용하는 템플릿 파일들은 앱 템플릿 디렉터리에 위치시킨다.
>
> ---
>
> ### Admin
>
> - 테이블의 내용을 열람하고 수정하는 기능을 제공한다.
> - 테이블에 들어 있는 내용들을 콘텐츠라고 하는데, Admin 사이트는 이 콘텐츠를 펹비하는 기능을 제공하는 것이다.
> - Admin 사이트에서 User와 Group 테이블을 포함해, 테이블에 대한 데이터의 입력, 수정, 삭제 등의 작업을 할 수 있다.
>
> ---
>
> ### runserver
>
> - 개발 과정에서 작성된 코드를 실행하고 테스트하는 테스트용 웹 서버이다.
>

<br/>

### Advantages of Django

- **Object-Relational Mapping (ORM) Support** − Django provides a bridge between the data model and the database engine, and supports a large set of database systems including MySQL, Oracle, Postgres, etc. Django also supports NoSQL database through Django-nonrel fork. For now, the only NoSQL databases supported are MongoDB and google app engine.
- **Multilingual Support** − Django supports multilingual websites through its built-in internationalization system. So you can develop your website, which would support multiple languages.
- **Framework Support** − Django has built-in support for Ajax, RSS, Caching and various other frameworks.
- **Administration GUI** − Django provides a nice ready-to-use user interface for administrative activities.
- **Development Environment** − Django comes with a lightweight web server to facilitate end-to-end application development and testing.

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
python .\manage.py createsuperuser

# Username (leave blank to use ''): root
# Email address: test@test.com
# Password: 1234 
# Password (again): 1234

python manage.py runserver
# Django version 4.1.7, using settings 'mysite.settings'
# Starting development server at http://127.0.0.1:8000/
```
