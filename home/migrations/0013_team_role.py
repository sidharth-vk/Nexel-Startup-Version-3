# Generated by Django 5.0.3 on 2024-06-24 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='role',
            field=models.CharField(default=1, max_length=250, verbose_name='Role'),
            preserve_default=False,
        ),
    ]