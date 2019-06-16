# Generated by Django 2.0.6 on 2018-12-16 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=7)),
                ('age', models.IntegerField()),
                ('pic', models.ImageField(upload_to='pics')),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]