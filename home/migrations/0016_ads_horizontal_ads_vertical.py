# Generated by Django 5.0.3 on 2024-07-29 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_terms_and_condition'),
    ]

    operations = [
        migrations.CreateModel(
            name='ads_horizontal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='ads/horizontal', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='ads_vertical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='ads/vertical', verbose_name='Image')),
            ],
        ),
    ]
