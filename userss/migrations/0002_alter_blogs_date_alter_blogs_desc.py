# Generated by Django 5.0.2 on 2024-02-22 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userss', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='desc',
            field=models.TextField(max_length=1000),
        ),
    ]
