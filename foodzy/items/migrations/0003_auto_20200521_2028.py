# Generated by Django 3.0.5 on 2020-05-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_transaction_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='accepter',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
