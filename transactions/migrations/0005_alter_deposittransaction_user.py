# Generated by Django 5.0.6 on 2024-06-20 22:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_alter_borrowingtransaction_user_and_more'),
        ('users', '0007_alter_userlibraryaccount_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposittransaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit_transactions', to='users.userlibraryaccount'),
        ),
    ]
