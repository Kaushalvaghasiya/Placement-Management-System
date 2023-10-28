# Generated by Django 3.1 on 2023-10-28 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0005_auto_20231028_1653'),
        ('job_management', '0002_auto_20231028_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user_management.studentprofile'),
        ),
        migrations.AlterField(
            model_name='job',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.employerprofile'),
        ),
    ]