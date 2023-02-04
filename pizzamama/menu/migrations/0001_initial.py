# Generated by Django 4.1.6 on 2023-02-04 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=64)),
                ('ingredients', models.CharField(max_length=256)),
                ('prix', models.FloatField(default=0)),
                ('vegetarienne', models.BooleanField(default=False)),
            ],
        ),
    ]