# Generated by Django 3.0 on 2020-09-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0031_assignment_writers_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
