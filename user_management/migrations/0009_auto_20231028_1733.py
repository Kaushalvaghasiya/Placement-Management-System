# Generated by Django 3.1 on 2023-10-28 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0008_auto_20231028_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]