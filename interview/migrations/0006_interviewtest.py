# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0005_auto_20150205_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_id', models.ForeignKey(to='interview.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
