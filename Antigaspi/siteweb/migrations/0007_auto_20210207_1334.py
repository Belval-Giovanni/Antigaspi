# Generated by Django 3.1.4 on 2021-02-07 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0006_auto_20210206_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img'),
        ),
    ]