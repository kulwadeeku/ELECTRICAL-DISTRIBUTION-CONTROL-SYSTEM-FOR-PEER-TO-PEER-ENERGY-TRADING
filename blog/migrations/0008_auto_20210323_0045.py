# Generated by Django 3.1.5 on 2021-03-22 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210323_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]