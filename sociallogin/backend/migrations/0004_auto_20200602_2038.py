# Generated by Django 3.0.6 on 2020-06-02 20:38

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200602_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='meta',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
