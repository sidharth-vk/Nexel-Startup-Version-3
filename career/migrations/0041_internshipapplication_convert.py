# Generated by Django 5.0.3 on 2024-07-23 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0040_alter_internship_assigned_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='internshipapplication',
            name='convert',
            field=models.BooleanField(default=1, verbose_name='Convert to intern'),
            preserve_default=False,
        ),
    ]
