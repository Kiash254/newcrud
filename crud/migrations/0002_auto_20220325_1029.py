# Generated by Django 2.2.22 on 2022-03-25 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Detail',
        ),
    ]