# Generated by Django 3.2.14 on 2022-08-09 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('houmer_id', models.BigIntegerField()),
                ('lat', models.DecimalField(decimal_places=10, max_digits=12)),
                ('lon', models.DecimalField(decimal_places=10, max_digits=12)),
                ('speed', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
