# Generated by Django 5.0.3 on 2024-06-07 17:44

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('edu', models.CharField(max_length=250, verbose_name='Education Required')),
                ('des', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('mode', models.CharField(max_length=250, verbose_name='Mode')),
                ('startdate', models.DateField(verbose_name='Start date')),
                ('duration', models.CharField(max_length=50, verbose_name='Duration')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('slug', models.CharField(blank=True, max_length=250, unique=True, verbose_name='Slug')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.category', verbose_name='Category')),
            ],
        ),
    ]
