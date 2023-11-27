# Generated by Django 4.2.6 on 2023-11-22 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(blank=True, max_length=300, null=True)),
                ('cuerpo', models.TextField()),
                ('autor', models.CharField(max_length=100)),
                ('fecha', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
