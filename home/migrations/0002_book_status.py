# Generated by Django 3.2.8 on 2021-11-06 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('available', 'available'), ('not available', 'not available')], default='available', max_length=13),
        ),
    ]