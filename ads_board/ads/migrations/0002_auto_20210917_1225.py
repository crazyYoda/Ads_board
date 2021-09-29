# Generated by Django 3.2.7 on 2021-09-17 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='category',
        ),
        migrations.RemoveField(
            model_name='ads',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='ads',
            name='content',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='authorUser',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
