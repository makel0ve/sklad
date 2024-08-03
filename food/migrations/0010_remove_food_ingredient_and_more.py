# Generated by Django 4.1.3 on 2022-11-05 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productone_delete_product'),
        ('food', '0009_foodingredient_alter_food_ingredient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='foodingredient',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='foodingredient',
            name='food',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_one', to='food.food'),
        ),
        migrations.AddField(
            model_name='foodingredient',
            name='ingredient_one',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_one', to='product.productone'),
        ),
    ]
