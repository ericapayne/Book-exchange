# Generated by Django 3.1.5 on 2021-05-04 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0011_auto_20210503_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='books',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookMng.book'),
        ),
    ]