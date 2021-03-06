# Generated by Django 3.0.7 on 2020-07-07 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WritersJoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=500)),
                ('last_name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=3)),
                ('phone', models.CharField(max_length=200)),
                ('additional_phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('confirm_password', models.CharField(max_length=200)),
                ('first_discipline', models.CharField(max_length=200)),
                ('second_discipline', models.CharField(max_length=200)),
                ('third_discipline', models.CharField(max_length=200)),
                ('fourth_discipline', models.CharField(max_length=200)),
                ('fifth_discipline', models.CharField(max_length=200)),
                ('academic_degree', models.CharField(max_length=200)),
                ('time_zone', models.CharField(max_length=200)),
                ('night_calls', models.BooleanField(default=False)),
            ],
        ),
    ]
