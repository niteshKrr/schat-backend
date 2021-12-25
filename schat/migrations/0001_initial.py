# Generated by Django 2.2.12 on 2021-12-25 10:09

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('user_1', models.CharField(max_length=20)),
                ('user_2', models.CharField(max_length=20)),
                ('msgs', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('phone_no', models.CharField(default='', max_length=12)),
                ('friends', jsonfield.fields.JSONField()),
            ],
        ),
    ]
