# Generated by Django 3.2 on 2021-12-13 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0006_descarticle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorttitlearticle',
            name='author',
        ),
        migrations.RemoveField(
            model_name='temporaryarticle',
            name='author',
        ),
        migrations.RemoveField(
            model_name='vipauthor',
            name='author_ptr',
        ),
        migrations.DeleteModel(
            name='DescArticle',
        ),
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('o', 'On review'), ('a', 'Approved'), ('p', 'Published')], default='d', max_length=1),
        ),
        migrations.DeleteModel(
            name='ShortTitleArticle',
        ),
        migrations.DeleteModel(
            name='TemporaryArticle',
        ),
        migrations.DeleteModel(
            name='VipAuthor',
        ),
    ]