# Generated by Django 5.0.3 on 2024-03-20 07:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calsy', '0005_details_interest1_details_interest2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='calsy.user_details'),
        ),
    ]
