# Generated by Django 3.1 on 2023-10-28 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0007_auto_20231028_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headprofile',
            name='full_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='full_name',
            field=models.CharField(max_length=100),
        ),
    ]
