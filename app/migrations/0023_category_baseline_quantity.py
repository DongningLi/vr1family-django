# Generated by Django 4.2 on 2023-05-16 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_recipientinformation_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='baseline_quantity',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
    ]