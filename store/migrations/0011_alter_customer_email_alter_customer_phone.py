# Generated by Django 4.2 on 2023-05-19 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_customer_name_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]