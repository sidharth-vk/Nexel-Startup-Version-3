# Generated by Django 5.0.3 on 2024-07-21 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0026_internship_assigned_offer_letter'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectreport',
            name='submission',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Rewrite', 'Rewrite'), ('Rejected', 'Rejected')], default=1, max_length=50, verbose_name='Submision'),
            preserve_default=False,
        ),
    ]
