# Generated by Django 5.0.3 on 2024-07-21 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0020_alter_internship_assigned_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship_assigned',
            name='start_date',
            field=models.DateField(auto_now=True, verbose_name='Date'),
        ),
    ]
