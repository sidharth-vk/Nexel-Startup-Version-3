# Generated by Django 5.0.3 on 2024-07-23 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0004_alter_profile_gender_alter_profile_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile',
            field=models.ImageField(blank=True, default='assets/images/profile_blank.png', upload_to='user/profile', verbose_name='Profile'),
        ),
    ]
