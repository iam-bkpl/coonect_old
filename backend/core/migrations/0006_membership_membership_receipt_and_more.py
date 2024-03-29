# Generated by Django 4.1 on 2023-06-11 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='membership_receipt',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='membership',
            name='passport_back',
            field=models.FileField(upload_to='passport'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='passport_front',
            field=models.FileField(upload_to='passport'),
        ),
    ]
