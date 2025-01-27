# Generated by Django 5.0.3 on 2024-06-26 16:52

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0006_career_shortdes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_of_issue', models.DateField(default=django.utils.timezone.now)),
                ('certificate_id', models.CharField(blank=True, max_length=20, unique=True)),
                ('certificate_image', models.URLField(blank=True, null=True)),
                ('internship_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.career')),
            ],
        ),
    ]
