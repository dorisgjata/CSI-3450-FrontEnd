# Generated by Django 2.1.4 on 2018-12-05 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0004_itemplaintexts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itemmaps',
            fields=[
                ('auto_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'itemmaps',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Itemstats',
            fields=[
                ('auto_id', models.AutoField(primary_key=True, serialize=False)),
                ('statvalue', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'itemstats',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Itemtags',
            fields=[
                ('auto_id', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'itemtags',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Languageitems',
            fields=[
                ('auto_id', models.AutoField(primary_key=True, serialize=False)),
                ('languageitem', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'languageitems',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('auto_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.IntegerField(blank=True, null=True)),
                ('mapsname', models.TextField(blank=True, null=True)),
                ('fullurl', models.TextField(blank=True, null=True)),
                ('spriteurl', models.TextField(blank=True, null=True)),
                ('x', models.IntegerField(blank=True, null=True)),
                ('y', models.IntegerField(blank=True, null=True)),
                ('w', models.IntegerField(blank=True, null=True)),
                ('h', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'maps',
                'managed': False,
            },
        ),
    ]
