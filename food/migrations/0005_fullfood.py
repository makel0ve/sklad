# Generated by Django 4.1.3 on 2022-11-04 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_food_ingredient3'),
    ]

    operations = [
        migrations.CreateModel(
            name='FullFood',
            fields=[
                ('food_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='food.food')),
            ],
            bases=('food.food',),
        ),
    ]
