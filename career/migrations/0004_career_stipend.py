# Generated by Django 5.0.3 on 2024-06-07 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0003_career_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='stipend',
            field=models.CharField(default=1, max_length=50, verbose_name='Stipend/paid/free'),
            preserve_default=False,
        ),
    ]