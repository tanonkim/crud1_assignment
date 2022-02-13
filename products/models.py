from django.db import models


class Drink(models.Model):
    category = models.ForeignKey(
        "Category", related_name="drinks", on_delete=models.CASCADE, null=True
    )
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField(max_length=300)

    class Meta:
        db_table = "drinks"


class Allergy(models.Model):
    name = models.CharField(max_length=45)
    drinks = models.ManyToManyField(
        Drink, related_name="allergies", through="AllergyDrink"
    )

    class Meta:
        db_table = "allergies"


class Category(models.Model):
    menu = models.ForeignKey(
        "Menu", related_name="categories", on_delete=models.CASCADE, null=True
    )
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "categories"


class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "menus"


class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sugars_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    protein_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    caffeine_mg = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    drink = models.ForeignKey(
        "Drink", related_name="nutritions", on_delete=models.CASCADE, null=True
    )
    size = models.ForeignKey(
        "Size", related_name="nutritions", on_delete=models.CASCADE, null=True
    )

    class Meta:
        db_table = "nuritions"


class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    drink = models.ForeignKey(
        "Drink", related_name="images", on_delete=models.CASCADE, null=True
    )

    class Meta:
        db_table = "images"


class AllergyDrink(models.Model):
    allergy = models.ForeignKey(
        "Allergy", related_name="allergydrinks", on_delete=models.CASCADE, null=True
    )
    drink = models.ForeignKey(
        "Drink", related_name="allergydrinks", on_delete=models.CASCADE, null=True
    )

    class Meta:
        db_table = "allergy_drinks"


class Size(models.Model):
    name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45, null=True)
    size_fluid_ounce = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = "sizes"
