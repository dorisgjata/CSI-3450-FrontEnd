# Generated by Django 2.1.4 on 2018-12-05 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0006_itemeffects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itembuildintos',
            fields=[
                ('auto_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'itembuildintos',
                'managed': False,
            },
        ),
    ]
