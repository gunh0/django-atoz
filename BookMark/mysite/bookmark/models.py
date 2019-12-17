from django.db import models
#from django.utils.encoding import python_2_unicode_compatible
from six import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible    # Python 2.x 지원용
class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)
    
    def __str__(self):  # 객체를 문자열로 표현할 때 사용하는 함수
        return self.title

    '''
    def __str__(self):  # 객체를 문자열로 표현할 때 사용하는 함수
        return "%s %s" %(self.title, self.url)
    '''