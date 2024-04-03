# Generated by Django 5.0.3 on 2024-03-26 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_initial_amount_item_original_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemissue',
            name='is_returned',
        ),
        migrations.RemoveField(
            model_name='itemreturned',
            name='all_returned',
        ),
        migrations.AlterField(
            model_name='itemissue',
            name='department',
            field=models.CharField(choices=[('Clothing', 'Clothing'), ('Food', 'Food'), ('Home', 'Home'), ('Outdoors', 'Outdoors'), ('Pet', 'Pet'), ('Security', 'Security'), ('Sports', 'Sports'), ('Tech', 'Tech'), ('Arts n Crafts', 'Arts n Crafts')], max_length=100),
        ),
    ]