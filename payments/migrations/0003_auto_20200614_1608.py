# Generated by Django 3.0.7 on 2020-06-14 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20200614_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermembership',
            name='membership',
            field=models.ForeignKey(default=4, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payments.Membership'),
        ),
    ]
