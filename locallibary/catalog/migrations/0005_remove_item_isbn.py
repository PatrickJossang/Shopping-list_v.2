# Generated by Django 4.1 on 2022-08-27 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_iteminstance_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='isbn',
        ),
    ]
