# Generated by Django 3.1.8 on 2023-10-27 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=300)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]