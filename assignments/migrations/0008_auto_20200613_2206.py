# Generated by Django 3.0.7 on 2020-06-13 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0007_auto_20200613_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
