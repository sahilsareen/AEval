# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0008_auto_20150206_0613'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InterviewTest',
            new_name='InterviewTestQuestion',
        ),
    ]
