# Generated by Django 3.2.14 on 2022-07-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]