# Generated by Django 3.2.15 on 2022-10-21 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view', '0004_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=500)),
            ],
        ),
    ]
