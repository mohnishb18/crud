# Generated by Django 3.2.15 on 2022-10-14 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
