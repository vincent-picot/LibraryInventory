# Generated by Django 2.1.7 on 2019-03-04 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn10', models.BigIntegerField()),
                ('isbn13', models.BigIntegerField(null=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('language', models.CharField(max_length=100)),
                ('release_date', models.DateTimeField()),
                ('price_new', models.IntegerField()),
                ('price_used', models.IntegerField(null=True)),
                ('authors', models.ManyToManyField(to='book.Author')),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'editors',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'genres',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('book_state', models.CharField(choices=[('N', 'New'), ('U', 'Used')], max_length=1)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='editor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='book.Editor'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='book.Genre'),
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('isbn10', 'isbn13')},
        ),
    ]