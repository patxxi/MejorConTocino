# Generated by Django 3.2.9 on 2021-11-19 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('type_food', models.CharField(max_length=255)),
                ('rating', models.IntegerField(null=True)),
                ('is_visited', models.BooleanField(default=False)),
            ],
        ),
    ]
