# Generated by Django 3.0 on 2020-08-13 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payments', '0007_order_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='support',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='support_order', to=settings.AUTH_USER_MODEL),
        ),
    ]
