# Generated by Django 2.1.15 on 2020-08-19 00:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_auto_20200819_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='foundation',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 19, 0, 34, 20, 61136, tzinfo=utc)),
        ),
    ]
