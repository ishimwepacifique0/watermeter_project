# Generated by Django 4.1.2 on 2022-10-17 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watermeter', '0003_employer_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(default='male', max_length=255),
        ),
        migrations.AddField(
            model_name='customer',
            name='phonenumber',
            field=models.CharField(default='947587986', max_length=255),
        ),
    ]