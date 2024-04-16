# Generated by Django 5.0.4 on 2024-04-16 02:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chinese', '0009_food_img_url_alter_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chinese.food')),
            ],
        ),
    ]