# Generated by Django 5.0.2 on 2024-04-20 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('href', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('named_url', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('menu', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu_app.menu')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu_app.menuitem')),
            ],
            options={
                'ordering': ['menu', 'id'],
            },
        ),
    ]