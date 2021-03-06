# Generated by Django 3.0.2 on 2020-02-15 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField()),
                ('comentario', models.TextField(max_length=200)),
                ('id_usuario_consum', models.IntegerField()),
                ('id_servico', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categ_nome', models.CharField(max_length=10)),
                ('principal', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomefantasia', models.CharField(max_length=60)),
                ('razaosocial', models.CharField(blank=True, max_length=60, null=True)),
                ('cnpj', models.CharField(blank=True, max_length=14, null=True)),
                ('formaspagto', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=100)),
                ('site', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_picture')),
                ('desc', models.TextField(max_length=200)),
                ('nota_media', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=3)),
                ('status', models.BooleanField(default=True)),
                ('categoria', models.ManyToManyField(to='servicos.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=100)),
                ('senha', models.CharField(max_length=8)),
                ('tel', models.CharField(blank=True, max_length=15, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='profile_picture')),
                ('dt_nasc', models.DateField(blank=True, null=True)),
                ('tpLograd', models.CharField(max_length=3)),
                ('lograd', models.CharField(max_length=40)),
                ('num', models.IntegerField()),
                ('compl', models.CharField(max_length=25)),
                ('bairro', models.CharField(max_length=20)),
                ('locali', models.CharField(max_length=30)),
                ('cep', models.CharField(max_length=8)),
                ('uf', models.CharField(max_length=2)),
                ('dt_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioServ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('usuario_serv', models.CharField(max_length=8)),
                ('senha', models.CharField(max_length=8)),
                ('email_usuario', models.CharField(max_length=60)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=11)),
                ('dt_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ddd', models.CharField(max_length=2)),
                ('num', models.CharField(max_length=9)),
                ('wp', models.CharField(max_length=1)),
                ('principal', models.CharField(max_length=1)),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servico_telefone', to='servicos.Servico')),
            ],
        ),
        migrations.AddField(
            model_name='servico',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.UsuarioServ'),
        ),
        migrations.CreateModel(
            name='HrFuncionamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=9)),
                ('horario', models.CharField(max_length=60)),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servico_horario', to='servicos.Servico')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tpLograd', models.CharField(max_length=3)),
                ('lograd', models.CharField(max_length=40)),
                ('num', models.IntegerField()),
                ('compl', models.CharField(max_length=25)),
                ('bairro', models.CharField(max_length=20)),
                ('locali', models.CharField(max_length=30)),
                ('cep', models.CharField(max_length=8)),
                ('uf', models.CharField(max_length=2)),
                ('gia', models.CharField(blank=True, max_length=4, null=True)),
                ('unidade', models.CharField(blank=True, max_length=4, null=True)),
                ('ibge', models.CharField(blank=True, max_length=4, null=True)),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servico_endereco', to='servicos.Servico')),
            ],
        ),
    ]
