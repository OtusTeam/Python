# Generated by Django 4.2.4 on 2023-12-14 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_animalcard'),
    ]

    operations = [
        migrations.AddField(
            model_name='wildanimal',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
