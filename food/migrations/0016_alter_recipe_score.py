# Generated by Django 4.1.1 on 2022-11-12 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productone_delete_product'),
        ('food', '0015_alter_recipe_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='score',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productone'),
        ),
    ]