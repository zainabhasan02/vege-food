# Generated by Django 3.2.20 on 2023-10-17 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_img',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
