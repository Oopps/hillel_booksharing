# Generated by Django 3.1.6 on 2021-04-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210401_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.FileField(default=True, null=True, upload_to=''),
        ),
    ]
