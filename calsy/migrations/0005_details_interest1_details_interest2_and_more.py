# Generated by Django 5.0.3 on 2024-03-18 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calsy', '0004_remove_details_duration1_remove_details_duration2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='Interest1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='Interest2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='Interest3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='Interest4',
            field=models.CharField(max_length=100, null=True),
        ),
    ]