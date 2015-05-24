# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeatPumpState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('power', models.BooleanField(default=False)),
                ('temperature', models.IntegerField(default=17)),
                ('mode', models.IntegerField(default=0)),
                ('fan', models.IntegerField(default=0)),
            ],
        ),
    ]
