# Generated by Django 5.0.4 on 2024-04-15 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinese', '0002_food_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(default='no_name', max_length=50),
        ),
    ]
