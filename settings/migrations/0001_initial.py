# Generated by Django 4.1.4 on 2022-12-21 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=60)),
                ('logo', models.ImageField(upload_to='settings/')),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('fb_link', models.URLField(max_length=500)),
                ('instagram_link', models.URLField(max_length=500)),
                ('twitter_link', models.URLField(max_length=500)),
            ],
        ),
    ]
