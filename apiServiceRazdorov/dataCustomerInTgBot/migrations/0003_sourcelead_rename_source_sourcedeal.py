# Generated by Django 4.1.5 on 2023-01-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataCustomerInTgBot', '0002_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceLead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idFromBitrix', models.IntegerField()),
                ('title', models.CharField(max_length=95)),
            ],
        ),
        migrations.RenameModel(
            old_name='Source',
            new_name='SourceDeal',
        ),
    ]
