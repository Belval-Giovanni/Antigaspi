# Generated by Django 3.1.4 on 2021-02-06 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0002_annonce'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='telephone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
