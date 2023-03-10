# Generated by Django 3.2.9 on 2023-02-26 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=250)),
                ('body', models.CharField(blank=True, max_length=500)),
                ('image', models.ImageField(upload_to='blog/images')),
            ],
        ),
    ]
