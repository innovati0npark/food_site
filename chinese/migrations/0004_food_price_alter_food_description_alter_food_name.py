# Generated by Django 5.0.4 on 2024-04-15 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinese', '0003_alter_food_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
