# Generated by Django 3.2.7 on 2021-09-25 14:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_delete_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
