# Generated by Django 4.0 on 2021-12-26 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='match',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='match',
            constraint=models.UniqueConstraint(fields=('name', 'stadium', 'date', 'time'), name='unique match per datetime and stadium'),
        ),
    ]
