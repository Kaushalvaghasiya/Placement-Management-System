# Generated by Django 3.1 on 2023-11-08 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_management', '0004_remove_application_resume'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Interview',
        ),
    ]
