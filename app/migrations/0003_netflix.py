# Generated by Django 3.1.2 on 2021-05-28 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210528_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Netflix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subscribers', models.IntegerField()),
                ('premium', models.IntegerField()),
                ('content', models.CharField(max_length=100)),
            ],
        ),
    ]
