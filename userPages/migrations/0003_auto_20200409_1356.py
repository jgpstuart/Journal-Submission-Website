# Generated by Django 3.0.4 on 2020-04-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userPages', '0002_auto_20200409_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proposal',
            old_name='reviewer_file',
            new_name='reviewer_1_file',
        ),
        migrations.AddField(
            model_name='proposal',
            name='reviewer_2_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='proposal',
            name='reviewer_3_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
