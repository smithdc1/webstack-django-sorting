# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-08 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SecretFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(blank=True, max_length=255, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('size', models.PositiveIntegerField(blank=True, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_secret', models.BooleanField(default=False)),
            ],
        ),
    ]
