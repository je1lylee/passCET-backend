# Generated by Django 2.2.1 on 2019-09-10 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passcet', '0013_passcet_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='paccet_ranklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('username', models.CharField(max_length=128)),
                ('totaltime', models.IntegerField()),
            ],
        ),
    ]
