# Generated by Django 5.0.3 on 2024-06-06 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_service_des'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.CharField(default=1, max_length=250, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]
