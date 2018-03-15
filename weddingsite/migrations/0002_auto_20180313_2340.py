# Generated by Django 2.0.3 on 2018-03-13 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddingsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='shabbat_dinner',
            field=models.NullBooleanField(choices=[(None, ''), (True, "Don't be meshuga, of course I'll be there!"), (False, "Az och un vai! I can't make it!")], default=None, verbose_name='\nWill you be able to attend Shabbat dinner on Friday, July 20th?\n\n'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='wedding_meal',
            field=models.CharField(blank=True, choices=[('malfatti', 'Ricotta and spinach malfatti with sage butter and parmesan crisps (vegetarian)'), ('curry', 'Red lentil coconut curry, grilled sweetcorn and courgette, and crisp rice balls (vegan)')], default='malfatti', max_length=200, verbose_name='\nAt the wedding, I would like to eat:\n\n'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='welcome_dietary_restrictions',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('Veggie', 'Vegetarian'), ('Vegan', 'Vegan'), ('GF', 'Gluten-free'), ('Kosh', 'No meat with milk'), ('Other', 'Other (please elaborate in comments section)')], default='None', max_length=6, verbose_name='\nDo you have any dietary restrictions?\n\n'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='welcome_dinner',
            field=models.NullBooleanField(choices=[(None, ''), (True, 'Definitely!'), (False, "I won't be able to make it")], default=None, verbose_name='\nWill you be able to attend the welcome dinner on Sunday, July 22nd?\n\n'),
        ),
    ]