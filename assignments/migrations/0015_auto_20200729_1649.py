# Generated by Django 3.0.8 on 2020-07-29 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assignments', '0014_auto_20200723_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writer',
            name='assignments',
        ),
        migrations.AddField(
            model_name='assignment',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_writer', to=settings.AUTH_USER_MODEL),
        ),
    ]