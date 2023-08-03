# Generated by Django 4.2 on 2023-05-16 06:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_donorinformation_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='aiditemrequest',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='donorinformation',
            name='hq_address',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donorinformation',
            name='is_individual',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='donorinformation',
            name='organisation_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donorinformation',
            name='preferred_communication_mode',
            field=models.CharField(choices=[('EMAIL', 'Email address'), ('PHONE', 'Phone'), ('MAIL', 'Mail')], default='EMAIL', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donorinformation',
            name='principal_contact_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='donorinformation',
            name='id_document_1_expiry_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipientfamilymember',
            name='id_document_1_expiry_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipientinformation',
            name='id_document_1_expiry_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]