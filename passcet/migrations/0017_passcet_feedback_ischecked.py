# Generated by Django 2.2.1 on 2019-11-07 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passcet', '0016_passcet_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='passcet_feedback',
            name='isChecked',
            field=models.BooleanField(default=False),
        ),
    ]