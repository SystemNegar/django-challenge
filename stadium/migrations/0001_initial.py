# Generated by Django 2.2 on 2021-12-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('founded_in', models.DateTimeField(editable=False)),
                ('capacity', models.IntegerField()),
            ],
        ),
    ]
