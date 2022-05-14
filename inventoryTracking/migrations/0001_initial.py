# Generated by Django 4.0.4 on 2022-05-14 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deletion_comment', models.TextField(max_length=2000)),
            ],
        ),
    ]