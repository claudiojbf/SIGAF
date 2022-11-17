# Generated by Django 3.2.16 on 2022-11-16 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modalidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_modalidade', models.CharField(max_length=50)),
            ],
            options={
                'db_table': '"atletas"."modalidade"',
            },
        ),
        migrations.CreateModel(
            name='SubDivisao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_divisao', models.CharField(max_length=10)),
                ('modalidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Atletas.modalidade')),
            ],
            options={
                'db_table': '"atletas"."subdivisao"',
            },
        ),
        migrations.CreateModel(
            name='Posicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicao', models.CharField(max_length=50)),
                ('modalidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Atletas.modalidade')),
            ],
            options={
                'db_table': '"atletas"."posicao"',
            },
        ),
        migrations.CreateModel(
            name='Atleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('apelido', models.CharField(blank=True, max_length=100, null=True)),
                ('data_nascimento', models.DateField()),
                ('rg', models.CharField(max_length=20, unique=True)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('perna_dominante', models.CharField(choices=[('D', 'Diretita'), ('E', 'Esquerda'), ('A', 'Ambidestro')], max_length=1)),
                ('matricula_escolar', models.CharField(blank=True, max_length=50, null=True)),
                ('serie', models.CharField(blank=True, max_length=50, null=True)),
                ('nivel_escolar', models.CharField(blank=True, max_length=50, null=True)),
                ('naturalidade_uf', models.CharField(max_length=2)),
                ('cidade', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=50)),
                ('numero_da_casa', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=11)),
                ('whatsapp', models.CharField(max_length=11)),
                ('whatsapp2', models.CharField(blank=True, max_length=11, null=True)),
                ('nome_pai', models.CharField(blank=True, max_length=50, null=True)),
                ('nome_mae', models.CharField(blank=True, max_length=50, null=True)),
                ('telefone_responsavel', models.CharField(blank=True, max_length=50, null=True)),
                ('telefone_responsavel2', models.CharField(blank=True, max_length=50, null=True)),
                ('altura', models.CharField(max_length=5)),
                ('peso', models.CharField(max_length=7)),
                ('plano_saude', models.CharField(blank=True, max_length=100, null=True)),
                ('alergia', models.CharField(default='Nenhuma', max_length=100, null=True)),
                ('foto_atleta', models.ImageField(blank=True, upload_to='FotoAtleta')),
                ('modalidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Atletas.modalidade')),
                ('posicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Atletas.posicao')),
            ],
            options={
                'db_table': '"atletas"."atleta"',
            },
        ),
    ]