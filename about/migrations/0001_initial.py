# Generated by Django 4.1.4 on 2022-12-21 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what_we_do', models.CharField(max_length=600)),
                ('our_mission', models.CharField(max_length=600)),
                ('our_goals', models.CharField(max_length=600)),
                ('image', models.ImageField(upload_to='about/')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=600)),
                ('description', models.CharField(max_length=600)),
            ],
        ),
    ]
