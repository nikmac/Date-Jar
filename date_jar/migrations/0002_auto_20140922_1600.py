# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('date_jar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.ManyToManyField(related_name=b'event', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
