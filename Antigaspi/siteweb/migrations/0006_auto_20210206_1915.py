# Generated by Django 3.1.4 on 2021-02-06 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0005_utilisateur_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='image',
            field=models.ImageField(null=True, upload_to='static/img'),
        ),
    ]