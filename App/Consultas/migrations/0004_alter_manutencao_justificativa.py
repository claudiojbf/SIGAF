# Generated by Django 3.2.16 on 2022-11-28 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consultas', '0003_alter_exametratamento_imagem_exame'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manutencao',
            name='justificativa',
            field=models.TextField(),
        ),
    ]
