# Generated by Django 3.0.4 on 2020-04-12 20:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('address', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('abstract', models.TextField(max_length=1000, null=True)),
                ('author_file', models.FileField(blank=True, null=True, upload_to='')),
                ('reviewer_1_file', models.FileField(blank=True, null=True, upload_to='')),
                ('reviewer_2_file', models.FileField(blank=True, null=True, upload_to='')),
                ('reviewer_3_file', models.FileField(blank=True, null=True, upload_to='')),
                ('editor_comments', models.TextField(default='none', max_length=12000, null=True)),
                ('status', models.TextField(choices=[('Submitted', 'Submitted'), ('Reviewed', 'Reviewed'), ('Major Revision', 'Major Revision'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Submitted', max_length=20)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('upload_date', models.DateTimeField(default=datetime.datetime(2020, 4, 12, 20, 39, 13, 976288, tzinfo=utc))),
                ('version', models.IntegerField(blank=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proposal_username_a', to=settings.AUTH_USER_MODEL)),
                ('reviewer_1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proposal_username_r1', to=settings.AUTH_USER_MODEL)),
                ('reviewer_2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proposal_username_r2', to=settings.AUTH_USER_MODEL)),
                ('reviewer_3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proposal_username_r3', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('institution', models.TextField(max_length=100)),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='journal_username', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_version', models.IntegerField(max_length=10)),
                ('comment_text', models.TextField(blank=True, max_length=500, null=True)),
                ('proposal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_proposal_id', to='userPages.Proposal')),
                ('reviewer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_username', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]