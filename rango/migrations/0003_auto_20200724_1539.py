# Generated by Django 3.0.8 on 2020-07-24 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20200724_1511'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-views'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['category']},
        ),
        migrations.AlterOrderWithRespectTo(
            name='category',
            order_with_respect_to=None,
        ),
        migrations.AlterOrderWithRespectTo(
            name='page',
            order_with_respect_to=None,
        ),
    ]
