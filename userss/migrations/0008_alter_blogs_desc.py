# Generated by Django 5.0.2 on 2024-02-23 07:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userss', '0007_alter_blogs_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='desc',
            field=ckeditor.fields.RichTextField(max_length=3000),
        ),
    ]
