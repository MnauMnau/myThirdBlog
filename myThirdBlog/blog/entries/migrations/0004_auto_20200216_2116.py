# Generated by Django 3.0.3 on 2020-02-16 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_auto_20200216_2101'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]
