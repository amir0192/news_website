# Generated by Django 4.2.2 on 2023-06-18 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News_category', '0002_rename_news_new_alter_news_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='type',
            new_name='name',
        ),
    ]
