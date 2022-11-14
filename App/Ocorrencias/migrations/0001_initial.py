# Generated by Django 3.2.16 on 2022-11-12 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Usuario', '0003_rename_data_de_criacao_usuario_data_de_registro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_local', models.CharField(max_length=30)),
            ],
            options={
                'db_table': '"facilitis"."local"',
            },
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_da_ocorrencia', models.CharField(max_length=100)),
                ('descricao_da_ocorrencia', models.TextField()),
                ('status', models.CharField(choices=[('ABT', 'Aberto'), ('EA', 'Em Andamento'), ('C', 'Concluido')], default='ABT', max_length=3)),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ocorrencias.local')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.usuario')),
            ],
            options={
                'db_table': '"facilitis"."ocorrencia"',
            },
        ),
    ]