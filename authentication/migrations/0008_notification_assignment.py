# Generated by Django 3.0.8 on 2020-08-04 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0019_remove_assignment_allowed_memberships'),
        ('authentication', '0007_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='assignment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assignments.Assignment'),
        ),
    ]
