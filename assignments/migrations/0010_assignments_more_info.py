# Generated by Django 3.0.7 on 2020-06-14 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0009_auto_20200614_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignments',
            name='more_info',
            field=models.TextField(max_length=1200, null=True),
        ),
    ]
