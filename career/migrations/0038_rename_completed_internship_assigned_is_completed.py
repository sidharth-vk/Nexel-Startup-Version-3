# Generated by Django 5.0.3 on 2024-07-21 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0037_alter_internship_assigned_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='internship_assigned',
            old_name='completed',
            new_name='is_completed',
        ),
    ]
