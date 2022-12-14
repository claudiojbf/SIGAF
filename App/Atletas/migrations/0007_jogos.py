# Generated by Django 3.2.16 on 2022-11-29 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Atletas', '0006_modalidade_imagem_modalidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('posicao', models.CharField(choices=[('T', 'Titular'), ('R', 'Reserva')], max_length=1)),
                ('minutos_jogados', models.DecimalField(decimal_places=2, max_digits=5)),
                ('gols', models.IntegerField()),
                ('finalizacoes', models.IntegerField()),
                ('toques', models.IntegerField()),
                ('passes_certos', models.IntegerField()),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Atletas.atleta')),
            ],
            options={
                'db_table': '"atletas"."jogos"',
            },
        ),
    ]
