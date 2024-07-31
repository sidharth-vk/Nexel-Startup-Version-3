# Generated by Django 5.0.3 on 2024-07-17 12:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0014_training'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speacial_Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.training', verbose_name='Training')),
            ],
        ),
        migrations.CreateModel(
            name='Training_FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2550, verbose_name='Question')),
                ('answer', models.TextField(verbose_name='Answer')),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.training', verbose_name='Training')),
            ],
        ),
        migrations.CreateModel(
            name='Training_Modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(max_length=50, verbose_name='Module')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('desc', models.TextField(verbose_name='Description')),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.training', verbose_name='Training')),
            ],
        ),
    ]