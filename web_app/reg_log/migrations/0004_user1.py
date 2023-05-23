# Generated by Django 4.2.1 on 2023-05-22 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_log', '0003_rename_pass1_user_pass_remove_user_pass2'),
    ]

    operations = [
        migrations.CreateModel(
            name='User1',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='Имя')),
                ('Surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('Email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('Pass1', models.CharField(max_length=20, verbose_name='Пароль')),
                ('Pass2', models.CharField(max_length=20, verbose_name='Пароль')),
                ('Age', models.IntegerField(verbose_name='Возраст')),
                ('Face', models.CharField(max_length=400, verbose_name='Фотография')),
                ('Balance', models.IntegerField(verbose_name='Баланс')),
            ],
        ),
    ]
