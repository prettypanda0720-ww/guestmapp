# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2020-08-01 19:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productType', models.IntegerField()),
                ('selectedTheme', models.IntegerField()),
                ('tires', models.IntegerField()),
                ('currency', models.CharField(blank=True, max_length=20)),
                ('price', models.IntegerField()),
                ('status', models.IntegerField()),
                ('createdTime', models.DateTimeField()),
                ('completedTime', models.DateTimeField()),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]