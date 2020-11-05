from bookmark.views import BookmarkLV, BookmarkDV
from django.urls import re_path

urlpatterns = [
    re_path(r"^$", BookmarkLV.as_view(), name="index"),
    re_path(r"^(?P<pk>\d+)/$", BookmarkDV.as_view(), name="detail"),
]
