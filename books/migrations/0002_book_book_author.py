# Generated by Django 5.0.6 on 2024-06-19 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
