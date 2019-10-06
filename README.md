# Django

### MTV (Model-Templat-View)

- Implement Project Body
- Model (models.py, admin.py)
- URLconf (urls.py)
- Views (views.py)
- Templates (templates/)



장고는 ‘웹 프레임워크’이며, 하나의 ‘애플리케이션’이다.

여러 사용자가 동시에 사이트에 접근할 경우, 이것을 처리하는 것은 ‘웹 서버’의 역할이다.

즉 python manage.py runserver 를 하면 웹 서버를 띄우기는 하지만,

단지 개발 테스트 용도로 제공해주는 것이다.

실제 배포할 경우에는 nginx 나 apache 같은 웹 서버가 필요하며,

웹 서버와 Python 애플리케이션인 장고가 통신할 수 있게 하는 WSGI(gunicorn, uwsgi 등)가 필요하다.

과거에는 Apache가 많이 사용되었으나,

Apache는 연결이 늘어나면 프로세스를 포크하는 방식인 반면,

Nginx는 Thread를 늘리는 방식이라, Nginx가 보다 더 많이 사용되고 있다.