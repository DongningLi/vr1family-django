# Generated by Django 4.2 on 2023-05-09 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_aiditemrequest_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name_plural': 'inventories'},
        ),
    ]
