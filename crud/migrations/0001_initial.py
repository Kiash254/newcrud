# Generated by Django 2.2.22 on 2022-03-20 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accname', models.CharField(max_length=90)),
                ('age', models.IntegerField()),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
