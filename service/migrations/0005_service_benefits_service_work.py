# Generated by Django 5.0.3 on 2024-06-06 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_alter_service_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='service_benefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benifits', models.CharField(max_length=250, verbose_name='benifits')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.service', verbose_name='service')),
            ],
        ),
        migrations.CreateModel(
            name='service_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(max_length=250, verbose_name='benifits')),
                ('des', models.CharField(max_length=2250, verbose_name='des')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.service', verbose_name='service')),
            ],
        ),
    ]
