# Generated by Django 3.1.4 on 2021-02-19 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_remove_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='noimage2.png', upload_to='staticfiles/media'),
        ),
    ]
