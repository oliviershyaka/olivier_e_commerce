# Generated by Django 4.2.9 on 2024-01-05 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerceApp', '0004_alter_register_email_alter_register_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phone_number',
            field=models.IntegerField(max_length=10),
        ),
    ]
