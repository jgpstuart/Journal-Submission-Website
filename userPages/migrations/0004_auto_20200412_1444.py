# Generated by Django 3.0.4 on 2020-04-12 20:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userPages', '0003_auto_20200412_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposal',
            name='editor_comments',
        ),
        migrations.AlterField(
            model_name='proposal',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 12, 20, 44, 42, 74818, tzinfo=utc)),
        ),
    ]