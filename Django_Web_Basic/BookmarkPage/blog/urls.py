from django.urls import re_path
from blog.views import *

urlpatterns = [
    # Example: /
    re_path(r"^$", PostLV.as_view(), name="index"),
    # Example: /post/ (same as /)
    re_path(r"^post/$", PostLV.as_view(), name="post_list"),
    # Example: /post/django-example/
    re_path(r"^post/(?P<slug>[-\w]+)/$", PostDV.as_view(), name="post_detail"),
    # Example: /archive/
    re_path(r"^archive/$", PostAV.as_view(), name="post_archive"),
    # Example: /2012/
    re_path(r"^(?P<year>\d{4})/$", PostYAV.as_view(), name="post_year_archive"),
    # Example: /2012/nov/
    re_path(
        r"^(?P<year>\d{4})/(?P<month>[a-z]{3})/$",
        PostMAV.as_view(),
        name="post_month_archive",
    ),
    # Example: /2012/nov/10/
    re_path(
        r"^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$",
        PostDAV.as_view(),
        name="post_day_archive",
    ),
    # Example: /today/
    re_path(r"^today/$", PostTAV.as_view(), name="post_today_archive"),
]
