# Generated by Django 5.1.3 on 2025-04-10 20:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_viatge_num_persones'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilUsuari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('nom_complet', models.CharField(blank=True, max_length=200, null=True)),
                ('pais_origen', models.CharField(blank=True, max_length=100, null=True)),
                ('data_naixement', models.DateField(blank=True, null=True)),
                ('usuari', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
