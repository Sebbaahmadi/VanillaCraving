# Generated by Django 4.0.4 on 2022-05-18 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0002_alter_home_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='text',
        ),
        migrations.RemoveField(
            model_name='home',
            name='title',
        ),
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
