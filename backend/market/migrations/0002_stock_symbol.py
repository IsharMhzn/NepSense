# Generated by Django 3.1.4 on 2020-12-29 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='symbol',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
