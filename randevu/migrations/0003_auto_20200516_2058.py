# Generated by Django 2.2.12 on 2020-05-16 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('randevu', '0002_mesajmezun_mesajogrenci'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mesajmezun',
            old_name='transkript',
            new_name='randevu',
        ),
        migrations.RenameField(
            model_name='mesajogrenci',
            old_name='transkript',
            new_name='randevu',
        ),
    ]
