# Generated by Django 3.2.8 on 2021-11-01 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_remove_isseubook_fine'),
    ]

    operations = [
        migrations.AddField(
            model_name='isseubook',
            name='fine',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
    ]
