# Generated by Django 5.0.6 on 2024-06-02 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userimage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserImage',
        ),
    ]
