# Generated by Django 4.2 on 2023-05-09 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_aiditem_itemkit_aidkititem_aidkit_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aidkit',
            name='items',
        ),
    ]