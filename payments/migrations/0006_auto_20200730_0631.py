# Generated by Django 3.0.8 on 2020-07-30 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0019_remove_assignment_allowed_memberships'),
        ('payments', '0005_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='assignment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assignments.Assignment'),
        ),
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
