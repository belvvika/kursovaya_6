# Generated by Django 5.1 on 2024-08-20 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_mailingattempt_client_mailingattempt_settings_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'permissions': [('can_view_any_mailings', 'Can view any mailings'), ('can_disable_mailings', 'Can disable mailings')], 'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
    ]
