# Generated by Django 5.0.3 on 2024-07-29 16:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career_dashboard', '0008_resources_file_data_resources_folder_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources_file_data',
            name='code',
            field=ckeditor.fields.RichTextField(default=1, verbose_name='Code'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resources_file_data',
            name='des',
            field=ckeditor.fields.RichTextField(default=1, verbose_name='Explanation'),
            preserve_default=False,
        ),
    ]
