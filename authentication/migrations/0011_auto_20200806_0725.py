# Generated by Django 3.0.8 on 2020-08-06 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_auto_20200806_0723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writer',
            name='confirm_password',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='password',
        ),
    ]
