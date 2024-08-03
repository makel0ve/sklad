# Generated by Django 4.1.3 on 2022-11-05 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productone_delete_product'),
        ('food', '0007_delete_foodfull'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='ingredient3',
        ),
        migrations.RemoveField(
            model_name='food',
            name='weigth',
        ),
        migrations.RemoveField(
            model_name='food',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='food',
            name='ingredient',
            field=models.ManyToManyField(null=True, related_name='ingredient', to='product.productone'),
        ),
    ]
