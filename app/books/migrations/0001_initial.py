# Generated by Django 3.1.6 on 2021-02-04 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('publish_year', models.PositiveSmallIntegerField()),
                ('review', models.CharField(max_length=512)),
            ],
        ),
    ]
