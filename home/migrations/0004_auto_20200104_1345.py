# Generated by Django 2.0 on 2020-01-04 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_filemodel_converted_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='converted_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
