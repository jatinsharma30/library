# Generated by Django 3.2.8 on 2021-11-02 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_isseubook_fine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='isseubook',
            name='fine',
        ),
    ]