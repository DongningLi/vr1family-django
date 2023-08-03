# Generated by Django 4.2 on 2023-05-09 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_inventory_donationdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aiditem',
            name='itemKit',
        ),
        migrations.CreateModel(
            name='AidKitItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.aiditem')),
                ('kit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.aidkit')),
            ],
        ),
        migrations.AddField(
            model_name='aidkit',
            name='items',
            field=models.ManyToManyField(through='app.AidKitItem', to='app.aiditem'),
        ),
    ]
