# Generated by Django 3.1.5 on 2021-01-31 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_auto_20210129_1021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='dimensoes',
            new_name='dimensao',
        ),
    ]
