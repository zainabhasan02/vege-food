# Generated by Django 3.2.20 on 2023-08-10 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='add_to_homepage',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='add_to_homepage'),
        ),
    ]