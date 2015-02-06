# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0007_auto_20150206_0538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interviewtest',
            old_name='interview_question_id',
            new_name='interview_question',
        ),
        migrations.AddField(
            model_name='interviewtest',
            name='score',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
