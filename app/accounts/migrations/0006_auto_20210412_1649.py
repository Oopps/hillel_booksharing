# Generated by Django 3.1.6 on 2021-04-12 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.FileField(default=True, null=True, upload_to='avatars'),
        ),
    ]
