# Generated by Django 2.1 on 2019-05-25 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(),
        ),
    ]
