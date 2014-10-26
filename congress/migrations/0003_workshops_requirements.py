# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('congress', '0002_workshops_placesavailable'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshops',
            name='requirements',
            field=models.CharField(default=b'Laptop', max_length=180, verbose_name='Requirements'),
            preserve_default=True,
        ),
    ]
