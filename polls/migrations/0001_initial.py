# Generated by Django 3.2 on 2023-06-16 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizz_id', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
