# Generated by Django 4.2 on 2024-10-24 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_remove_new_region_delete_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
