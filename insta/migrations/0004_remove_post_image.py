# Generated by Django 3.1.2 on 2020-10-21 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_auto_20201021_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]