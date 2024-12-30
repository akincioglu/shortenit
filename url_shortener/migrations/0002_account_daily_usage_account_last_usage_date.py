# Generated by Django 5.1.4 on 2024-12-30 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='daily_usage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='last_usage_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]