# Generated by Django 3.0.8 on 2020-08-06 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_auto_20200806_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='last_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='writer',
            name='password',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='writer',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]