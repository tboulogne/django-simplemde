# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 17:51
from __future__ import unicode_literals

from django.db import migrations, models
import simplemde.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Markdown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('content', simplemde.fields.SimpleMDEField()),
            ],
        ),
    ]