# Generated by Django 3.1 on 2023-10-28 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_management', '0004_auto_20231028_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('application_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('application_deadline', models.DateField()),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.employer')),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_date', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_management.application')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_management.job'),
        ),
    ]
