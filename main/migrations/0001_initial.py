# Generated by Django 5.1.1 on 2024-09-16 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Your name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email address')),
                ('country', models.CharField(max_length=50, verbose_name='Select your country')),
                ('phone', models.PositiveIntegerField(verbose_name='Your Phone')),
                ('company', models.CharField(max_length=50, verbose_name='Scam company name')),
                ('lost', models.CharField(max_length=50, verbose_name='Amount lost')),
                ('currency', models.CharField(max_length=50, verbose_name='Currency')),
                ('transfer', models.CharField(max_length=50, verbose_name='Transfer method')),
                ('date', models.DateField(max_length=50, verbose_name='Last transaction date')),
                ('story', models.TextField(verbose_name='Tell your story')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]