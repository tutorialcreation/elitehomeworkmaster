# Generated by Django 3.0 on 2020-09-01 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0029_auto_20200901_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='location',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
