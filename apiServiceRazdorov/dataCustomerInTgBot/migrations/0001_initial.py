# Generated by Django 4.1.5 on 2023-01-21 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllManagers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idManager', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=95)),
            ],
        ),
    ]
