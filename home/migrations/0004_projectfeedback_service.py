# Generated by Django 5.0.3 on 2024-06-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectfeedback',
            name='service',
            field=models.CharField(default=1, max_length=250, verbose_name='Service done'),
            preserve_default=False,
        ),
    ]