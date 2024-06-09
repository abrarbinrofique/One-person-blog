# Generated by Django 4.2.11 on 2024-06-08 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('bio', models.CharField(max_length=50)),
                ('phone', models.IntegerField(max_length=15)),
            ],
        ),
    ]
