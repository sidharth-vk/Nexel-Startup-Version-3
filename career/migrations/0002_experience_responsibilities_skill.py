# Generated by Django 5.0.3 on 2024-06-07 17:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Experience')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.career', verbose_name='Career')),
            ],
        ),
        migrations.CreateModel(
            name='responsibilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Responsibilities')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.career', verbose_name='Career')),
            ],
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Skills')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.career', verbose_name='Career')),
            ],
        ),
    ]