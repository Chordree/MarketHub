# Generated by Django 4.2 on 2023-07-26 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilorin', '0003_alter_category_options_alter_photo_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photo',
            new_name='Product',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]
