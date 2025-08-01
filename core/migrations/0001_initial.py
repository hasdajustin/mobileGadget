# Generated by Django 5.2.4 on 2025-07-29 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioGear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='audio_gear_images/')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
