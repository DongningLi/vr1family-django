# Generated by Django 4.2 on 2023-05-11 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_recipientfamilymember_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorinformation',
            name='age',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
