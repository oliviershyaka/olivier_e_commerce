# Generated by Django 4.2.9 on 2024-01-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerceApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phone_number',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='register',
            name='user_role',
            field=models.CharField(default='user', max_length=255),
        ),
    ]
