# Generated by Django 3.2.7 on 2021-09-09 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_remove_pizza_tagline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topping',
            old_name='name',
            new_name='topping',
        ),
    ]
