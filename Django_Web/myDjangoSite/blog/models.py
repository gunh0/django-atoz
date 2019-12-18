from __future__ import unicode_literals
from six import python_2_unicode_compatible

from django.db import models
from django.urls import reverse

# Create your models here.

@python_2_unicode_compatible
class Post(models.Model):
    objects = models.Manager()
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField(
        'SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    dsecription = models.CharField(
        'DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Data', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'my_post'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))