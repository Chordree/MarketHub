# Generated by Django 4.2 on 2023-07-31 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilorin', '0004_rename_photo_product_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]