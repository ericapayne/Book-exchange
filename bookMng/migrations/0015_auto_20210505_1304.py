# Generated by Django 3.1.5 on 2021-05-05 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0014_wish_web'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='web',
            field=models.URLField(),
        ),
    ]