# Generated by Django 5.0.3 on 2024-06-09 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_projectfeedback_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectfeedback',
            name='slug',
            field=models.CharField(blank=True, max_length=250, unique=True, verbose_name='Slug'),
        ),
    ]
