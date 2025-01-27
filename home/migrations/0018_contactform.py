# Generated by Django 5.0.3 on 2024-07-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_privacy_policy'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('company', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
