# Generated by Django 5.1 on 2024-08-20 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'permissions': [('can_view_the_list_of_service_users', 'Can view the list of service users'), ('can_block_users_of_the_service', 'Can block users of the service')], 'verbose_name': 'Пользователь', 'verbose_name_plural': ('Пользователи',)},
        ),
    ]
