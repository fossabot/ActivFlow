# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-25 07:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Creation Date')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name=b'Last Updated')),
                ('status', models.CharField(choices=[(b'Initiated', b'Initiated'), (b'Draft', b'Draft'), (b'Submitted', b'Submitted'), (b'Withdrawn', b'Withdrawn'), (b'Completed', b'Completed')], max_length=30, verbose_name=b'Status')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Creation Date')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name=b'Last Updated')),
                ('status', models.CharField(choices=[(b'Not Started', b'Not Started'), (b'In Progress', b'In Progress'), (b'Ended', b'Ended')], max_length=30, verbose_name=b'Status')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Request')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
