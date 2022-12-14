# Generated by Django 4.0 on 2022-01-24 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idproof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadharid', models.CharField(max_length=16)),
                ('voterid', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('qualification', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=10)),
                ('idproof', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='OneToOne.idproof')),
            ],
        ),
    ]
