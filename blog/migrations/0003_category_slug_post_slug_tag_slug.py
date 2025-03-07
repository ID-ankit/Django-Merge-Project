# Generated by Django 5.1.6 on 2025-03-04 07:01

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='tittle'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='name'),
            preserve_default=False,
        ),
    ]
