# Generated by Django 5.0.3 on 2024-06-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0007_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='certificate_image',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]