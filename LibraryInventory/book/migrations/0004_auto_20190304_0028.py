# Generated by Django 2.1.7 on 2019-03-04 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20190304_0024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='editor_id',
            new_name='editor',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='genre_id',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='language_id',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='book_id',
            new_name='book',
        ),
        migrations.AlterModelTable(
            name='language',
            table='languages',
        ),
    ]