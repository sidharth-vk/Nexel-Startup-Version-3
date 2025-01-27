# Generated by Django 5.0.3 on 2024-07-16 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0012_career_code_alter_offerletter_certificate_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternshipApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('internship_for', models.CharField(max_length=255)),
                ('college_name', models.CharField(max_length=255)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
