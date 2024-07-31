# Generated by Django 5.0.3 on 2024-06-06 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='companyname',
            field=models.CharField(default=1, max_length=50, verbose_name='Company Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projects',
            name='cardimg',
            field=models.ImageField(upload_to='project/card/', verbose_name='Card Image'),
        ),
    ]
