# Generated by Django 4.2 on 2023-05-09 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_aiditemrequest_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestKit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('kit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.aidkit')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.aiditemrequest')),
            ],
        ),
    ]
