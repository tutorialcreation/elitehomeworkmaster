# Generated by Django 3.0 on 2020-09-25 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0035_auto_20200921_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='viewed',
            field=models.BooleanField(default=False),
        ),
    ]
