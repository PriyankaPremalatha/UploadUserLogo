# Generated by Django 3.0.3 on 2020-04-11 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
