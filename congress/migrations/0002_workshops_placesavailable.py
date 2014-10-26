# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('congress', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshops',
            name='placesAvailable',
            field=models.IntegerField(default=20, verbose_name='Places available'),
            preserve_default=True,
        ),
    ]
