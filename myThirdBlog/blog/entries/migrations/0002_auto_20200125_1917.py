# Generated by Django 3.0.1 on 2020-01-25 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries'},
        ),
        migrations.AddField(
            model_name='entry',
            name='entry_nViews',
            field=models.IntegerField(default=0),
        ),
    ]
