# Generated by Django 4.1.3 on 2022-12-14 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='Moshina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=21)),
                ('rang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.rang')),
            ],
        ),
    ]
