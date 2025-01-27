# Generated by Django 5.0.3 on 2024-03-25 02:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_amount', models.PositiveBigIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveBigIntegerField()),
                ('issued_to', models.CharField(max_length=100)),
                ('department', models.CharField(choices=[('Clothing', 'Clothing'), ('Food', 'Food'), ('Home', 'Home'), ('Outdoors', 'Outdoors'), ('Pet', 'Pet'), ('Security', 'Security'), ('Sports', 'Sports'), ('Tech', 'Tech')], max_length=100)),
                ('date_issued', models.DateTimeField(auto_now_add=True)),
                ('date_returned', models.DateField()),
                ('is_returned', models.BooleanField(default=False)),
                ('issued_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemReturned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_returned', models.DateField(auto_now_add=True)),
                ('amount_returned', models.PositiveIntegerField()),
                ('all_returned', models.BooleanField(default=False)),
                ('returner', models.CharField(max_length=100)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.item')),
            ],
        ),
        migrations.CreateModel(
            name='RestockItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.item')),
            ],
        ),
    ]
