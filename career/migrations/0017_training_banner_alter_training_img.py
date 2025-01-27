# Generated by Django 5.0.3 on 2024-07-17 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0016_training_price_training_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='banner',
            field=models.ImageField(default=1, upload_to='training/banner', verbose_name='Banner Image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='training',
            name='img',
            field=models.ImageField(upload_to='training', verbose_name='card Image'),
        ),
    ]
