# Generated by Django 3.2.7 on 2021-09-25 15:03

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_alter_ads_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
