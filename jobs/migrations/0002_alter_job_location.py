# Generated by Django 4.2 on 2023-04-19 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(choices=[('Maseno', 'Maseno'), ('Nairobi', 'Nairobi'), ('Kisumu', 'Kisumu'), ('Remote', 'Remote')], max_length=50),
        ),
    ]
