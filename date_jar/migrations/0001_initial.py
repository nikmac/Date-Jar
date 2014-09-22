# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=50)),
                ('url', models.URLField(null=True, blank=True)),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
                ('image', models.URLField(null=True, blank=True)),
                ('done', models.BooleanField(default=False)),
                ('category', models.ForeignKey(related_name=b'event', to='date_jar.Category')),
                ('user', models.ManyToManyField(related_name=b'event', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
