# Generated by Django 3.0.8 on 2020-07-30 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0017_assignment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.CharField(blank=True, choices=[('APP', 'Approved'), ('PEN', 'Pending'), ('COMP', 'Completed'), ('REV', 'Revision'), ('BID', 'Not Yet Bidded'), ('PRIV', 'Private')], default='PRIV', max_length=23, null=True),
        ),
    ]
