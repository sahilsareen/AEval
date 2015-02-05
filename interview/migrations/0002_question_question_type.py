# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(default=b'general', max_length=24, choices=[(b'array', b'Arrays'), (b'linked_list', b'Linked Lists'), (b'hash_map', b'Hash Maps'), (b'stack', b'Stacks'), (b'queue', b'Queues'), (b'tree', b'Trees'), (b'graph', b'Graphs'), (b'heap', b'Heaps'), (b'trie', b'Tries'), (b'networking', b'Computer Networking'), (b'os', b'Operating Systems'), (b'general', b'General Questions')]),
            preserve_default=True,
        ),
    ]
