# Generated by Django 4.2.2 on 2023-06-30 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_job_company'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Job',
        ),
    ]
