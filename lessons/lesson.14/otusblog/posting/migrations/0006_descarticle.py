# Generated by Django 3.2 on 2021-12-09 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0005_temporaryarticle'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescArticle',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('posting.article',),
        ),
    ]