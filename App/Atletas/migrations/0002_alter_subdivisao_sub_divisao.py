# Generated by Django 3.2.16 on 2022-11-16 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atletas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdivisao',
            name='sub_divisao',
            field=models.CharField(max_length=20),
        ),
    ]
