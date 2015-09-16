# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0002_auto_20150909_2126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='image',
            new_name='photo',
        ),
    ]
