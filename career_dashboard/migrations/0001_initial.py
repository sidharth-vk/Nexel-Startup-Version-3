# Generated by Django 5.0.3 on 2024-07-25 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Category')),
                ('logo', models.ImageField(upload_to='resources/category', verbose_name='Icon')),
            ],
        ),
    ]