# Generated by Django 3.2.20 on 2023-08-19 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_product_product_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomepageBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image', models.ImageField(upload_to='banner_images')),
                ('banner_text', models.CharField(blank=True, max_length=255, null=True)),
                ('banner_url', models.CharField(blank=True, max_length=255, null=True)),
                ('button_text', models.CharField(blank=True, max_length=100, null=True)),
                ('active_banner', models.BooleanField(blank=True, default=True, null=True)),
                ('order_banner', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['banner_text'],
            },
        ),
    ]
