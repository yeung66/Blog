from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    tag = models.CharField(max_length=10, blank=True)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering=['-publish_date']