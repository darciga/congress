# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('lastName', models.CharField(max_length=80, verbose_name='LastName')),
                ('email', models.EmailField(max_length=75, verbose_name='Email')),
                ('address', models.CharField(max_length=140, verbose_name='Address')),
                ('city', models.CharField(max_length=90, verbose_name='City')),
                ('telephone', models.CharField(max_length=30, verbose_name='Telephone')),
                ('placeOrigin', models.CharField(help_text=b'Company or institute', max_length=180, verbose_name='Place of origin')),
            ],
            options={
                'verbose_name': 'Applicant',
                'verbose_name_plural': 'Applicants',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('objective', models.TextField(verbose_name='Objective')),
                ('dateBegin', models.DateField(verbose_name='Date begin')),
                ('dateEnd', models.DateField(verbose_name='Date end')),
                ('hourBegin', models.CharField(max_length=10, verbose_name='Hour Begin')),
                ('hourEnd', models.CharField(max_length=10, verbose_name='Hour end')),
                ('place', models.CharField(max_length=40, verbose_name='Place')),
            ],
            options={
                'verbose_name': 'Conference',
                'verbose_name_plural': 'Conferences',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rapporteur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('lastName', models.CharField(max_length=80, verbose_name='LastName')),
                ('email', models.EmailField(max_length=75, verbose_name='Email')),
                ('address', models.CharField(max_length=140, verbose_name='Address')),
                ('city', models.CharField(max_length=90, verbose_name='City')),
                ('telephone', models.CharField(max_length=30, verbose_name='Telephone')),
                ('company', models.CharField(help_text=b'Company or institution', max_length=160, verbose_name='Company')),
            ],
            options={
                'verbose_name': 'Rapporteur',
                'verbose_name_plural': 'Rapporteurs',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Workshops',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('objective', models.TextField(verbose_name='Objective')),
                ('dateBegin', models.DateField(verbose_name='Date begin')),
                ('dateEnd', models.DateField(verbose_name='Date end')),
                ('hourBegin', models.CharField(max_length=10, verbose_name='Hour Begin')),
                ('hourEnd', models.CharField(max_length=10, verbose_name='Hour end')),
                ('place', models.CharField(max_length=40, verbose_name='Place')),
                ('placesAvailable', models.IntegerField(default=20, verbose_name='Places available')),
                ('requirements', models.CharField(default=b'Laptop', max_length=180, verbose_name='Requirements')),
                ('rapporteur', models.ForeignKey(related_name='Rapporteur', to='congress.Rapporteur')),
            ],
            options={
                'verbose_name': 'Workshop',
                'verbose_name_plural': 'Workshops',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='conference',
            name='rapporteur',
            field=models.ForeignKey(related_name='Lecturer', to='congress.Rapporteur'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='applicants',
            name='conference',
            field=models.ManyToManyField(to='congress.Conference', verbose_name=b'Conference'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='applicants',
            name='workshop',
            field=models.ManyToManyField(to='congress.Workshops', verbose_name=b'Workshop'),
            preserve_default=True,
        ),
    ]
