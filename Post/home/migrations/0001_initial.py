# Generated by Django 3.1.4 on 2021-08-28 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='intresting_url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('company', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=40)),
                ('validthrough', models.DateField(max_length=20)),
                ('datePosted', models.DateField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='unintresting_url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
    ]