# Generated by Django 5.1.6 on 2025-02-27 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Spreadsheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column', models.IntegerField()),
                ('value', models.TextField(blank=True, null=True)),
                ('formula', models.TextField(blank=True, null=True)),
                ('row', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cells', to='sheets.row')),
            ],
        ),
        migrations.AddField(
            model_name='row',
            name='spreadsheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rows', to='sheets.spreadsheet'),
        ),
    ]
