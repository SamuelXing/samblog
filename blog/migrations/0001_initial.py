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
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('summary', models.CharField(max_length=200, verbose_name='\u6458\u8981')),
                ('content', models.TextField(verbose_name='\u6b63\u6587')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('number', models.IntegerField(default=0, verbose_name='\u6587\u7ae0\u6570')),
            ],
            options={
                'ordering': ['-number'],
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='cat_name',
            field=models.ForeignKey(default=b'', verbose_name='\u5206\u7c7b ', to='blog.Category', null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='user_name',
            field=models.ForeignKey(verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL),
        ),
    ]
