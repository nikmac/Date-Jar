from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class Event(models.Model):
    category = models.ForeignKey(Category, related_name='event')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=50)
    url = models.URLField(blank=True, null=True)
    address = models.CharField(blank=True, null=True, max_length=100)
    image = models.URLField(blank=True, null=True)
    done = models.BooleanField(default=False)
    user = models.ManyToManyField(User, null=True, blank=True, related_name='event')

    def __unicode__(self):
        return self.name
