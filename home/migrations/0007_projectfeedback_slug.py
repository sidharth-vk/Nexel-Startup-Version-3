# Generated by Django 5.0.3 on 2024-06-09 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_projectfeedback_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectfeedback',
            name='slug',
            field=models.CharField(blank=True, max_length=250, verbose_name='Slug'),
        ),
    ]
