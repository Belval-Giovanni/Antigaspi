# Generated by Django 3.1.4 on 2021-02-07 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0007_auto_20210207_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img'),
        ),
    ]
