# Generated by Django 3.1 on 2023-11-06 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_management', '0003_auto_20231028_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='resume',
        ),
    ]