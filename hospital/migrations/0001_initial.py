# Generated by Django 4.0.6 on 2023-03-22 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_group', models.CharField(max_length=5)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
