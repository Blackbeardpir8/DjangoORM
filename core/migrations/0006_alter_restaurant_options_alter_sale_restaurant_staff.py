# Generated by Django 5.1.1 on 2024-11-03 05:20

import django.db.models.deletion
import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_rating_rating_alter_rating_restaurant_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurant',
            options={'get_latest_by': 'date_opened', 'ordering': [django.db.models.functions.text.Lower('name'), 'date_opened']},
        ),
        migrations.AlterField(
            model_name='sale',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales', to='core.restaurant'),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('restaurants', models.ManyToManyField(to='core.restaurant')),
            ],
        ),
    ]
