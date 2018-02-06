# Generated by Django 2.0 on 2018-02-06 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddingsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=128, unique=True)),
                ('category', models.CharField(blank=True, max_length=20, null=True)),
                ('shabbat_dinner', models.NullBooleanField(default=None)),
                ('welcome_dinner', models.BooleanField(default=False)),
            ],
        ),
    ]
