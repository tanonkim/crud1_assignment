# Generated by Django 4.0.2 on 2022-02-11 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergy',
            name='drinks',
            field=models.ManyToManyField(related_name='allergies', through='products.AllergyDrink', to='products.Drink'),
        ),
        migrations.AlterField(
            model_name='allergydrink',
            name='allergy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allergydrinks', to='products.allergy'),
        ),
        migrations.AlterField(
            model_name='allergydrink',
            name='drink',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allergydrinks', to='products.drink'),
        ),
        migrations.AlterField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='products.menu'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='drinks', to='products.category'),
        ),
        migrations.AlterField(
            model_name='image',
            name='drink',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.drink'),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='drink',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nutritions', to='products.drink'),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nutritions', to='products.size'),
        ),
    ]
