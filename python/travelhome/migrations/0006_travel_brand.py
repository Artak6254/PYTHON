# Generated by Django 5.1.4 on 2025-01-26 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelhome', '0005_travel_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel_Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_img', models.ImageField(blank=True, default='jpg', upload_to='image')),
            ],
        ),
    ]
