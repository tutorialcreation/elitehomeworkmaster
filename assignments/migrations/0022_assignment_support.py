# Generated by Django 3.0 on 2020-08-13 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assignments', '0021_assignment_return_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='support',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_support', to=settings.AUTH_USER_MODEL),
        ),
    ]