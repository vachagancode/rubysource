# Generated by Django 4.2.4 on 2023-08-11 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_resources'),
    ]

    operations = [
        migrations.CreateModel(
            name='CopyrightRules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copyright_rule', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'CopyrightRules',
            },
        ),
    ]