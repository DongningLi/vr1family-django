# Generated by Django 4.2 on 2023-05-11 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_category_options_alter_inventory_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipientfamilymember',
            name='age',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipientinformation',
            name='age',
            field=models.IntegerField(),
        ),
    ]
