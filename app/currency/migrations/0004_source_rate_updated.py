# Generated by Django 5.0.4 on 2024-05-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_contactus_rename_type_rate_currency_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_name', models.CharField(max_length=64)),
                ('source_url', models.URLField(max_length=256)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='rate',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
