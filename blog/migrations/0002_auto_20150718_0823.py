# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='name',
            new_name='blogname',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='catname',
        ),
    ]
