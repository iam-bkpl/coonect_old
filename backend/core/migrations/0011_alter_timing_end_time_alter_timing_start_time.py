# Generated by Django 4.1 on 2023-06-15 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_eventfeatures_contact_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timing',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='timing',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
