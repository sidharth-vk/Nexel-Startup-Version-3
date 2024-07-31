# Generated by Django 5.0.3 on 2024-07-25 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=500, verbose_name='Github Link')),
                ('resources', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career_dashboard.resources', verbose_name='Resources')),
            ],
        ),
    ]