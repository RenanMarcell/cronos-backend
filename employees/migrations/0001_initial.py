# Generated by Django 3.2.11 on 2022-01-31 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
                ('hire_date', models.DateField()),
            ],
        ),
    ]
