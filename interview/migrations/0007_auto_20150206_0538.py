# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0006_interviewtest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interviewtest',
            old_name='question_id',
            new_name='interview_question_id',
        ),
    ]
