# Generated by Django 3.0 on 2020-08-24 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0026_remove_assignment_thread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.CharField(blank=True, choices=[('APP', 'Approved'), ('PEN', 'Ongoing'), ('COMP', 'Completed'), ('REV', 'Return for Revision'), ('BID', 'Accept'), ('PRIV', 'Private')], default='PRIV', max_length=23, null=True),
        ),
    ]