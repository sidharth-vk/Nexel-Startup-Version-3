# Generated by Django 5.0.3 on 2024-06-09 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_projectfeedback_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectfeedback',
            name='slug',
            field=models.CharField(blank=True, max_length=250, unique=True, verbose_name='Slug'),
        ),
    ]
