# Generated by Django 5.0.6 on 2024-06-21 21:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_alter_deposittransaction_user'),
        ('users', '0007_alter_userlibraryaccount_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowingtransaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userlibraryaccount'),
        ),
    ]
