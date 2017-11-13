# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datawarga', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warga',
            name='imigrasi',
            field=models.ForeignKey(verbose_name=b'Dokumen Imigrasi', blank=True, to='datawarga.DocImigrasi'),
        ),
    ]
