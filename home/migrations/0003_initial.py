# Generated by Django 5.0.3 on 2024-06-09 11:11

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_delete_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('comapny', models.CharField(max_length=250, verbose_name='Company Name')),
                ('logo', models.ImageField(upload_to='feedback/company', verbose_name='Logo')),
                ('des', models.CharField(max_length=250, verbose_name='Designation')),
                ('content', ckeditor.fields.RichTextField(verbose_name='feedback')),
                ('rating', models.PositiveIntegerField()),
            ],
        ),
    ]
