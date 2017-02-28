# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pic', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('room_code', models.CharField(default=uuid.uuid4, max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='picture',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoApp.room'),
        ),
    ]