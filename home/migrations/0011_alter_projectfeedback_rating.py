# Generated by Django 5.0.3 on 2024-06-09 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_projectfeedback_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectfeedback',
            name='rating',
            field=models.CharField(max_length=50, verbose_name='Positive Integer(12345)'),
        ),
    ]
