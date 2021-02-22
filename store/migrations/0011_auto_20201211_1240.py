# Generated by Django 3.0.3 on 2020-12-11 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20201207_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.TextField(blank=True, default='', max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='composition',
            field=models.TextField(blank=True, default='', max_length=1200),
        ),
    ]
