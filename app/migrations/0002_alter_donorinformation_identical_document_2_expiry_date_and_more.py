# Generated by Django 4.2 on 2023-05-01 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorinformation',
            name='Identical_Document_2_expiry_Date',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='donorinformation',
            name='Identical_Document_3_expiry_Date',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='donorinformation',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
