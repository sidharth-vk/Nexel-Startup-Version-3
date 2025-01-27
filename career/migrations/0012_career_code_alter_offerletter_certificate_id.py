# Generated by Django 5.0.3 on 2024-07-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0011_alter_offerletter_certificate_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='code',
            field=models.CharField(default=1, max_length=50, verbose_name='Code'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offerletter',
            name='certificate_id',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
