# Generated by Django 5.0.3 on 2024-07-21 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
        ('career', '0017_training_banner_alter_training_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='no_of_weeks',
            field=models.IntegerField(default=4, verbose_name='no_of_weeks'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Internship_Assigned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.career', verbose_name='Internship For')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.profile', verbose_name='User')),
            ],
        ),
    ]
