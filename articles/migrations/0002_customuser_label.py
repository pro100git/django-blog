# Generated by Django 3.1.1 on 2020-09-29 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='label',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
