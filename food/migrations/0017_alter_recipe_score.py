# Generated by Django 4.1.1 on 2022-11-12 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0016_alter_recipe_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='score',
            field=models.IntegerField(null=True),
        ),
    ]
