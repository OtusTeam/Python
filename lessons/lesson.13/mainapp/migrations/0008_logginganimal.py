# Generated by Django 4.2.4 on 2023-12-14 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_wildanimal_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoggingAnimal',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('mainapp.animal',),
        ),
    ]