import json

from django.http import JsonResponse
from django.views import View

from products.models import Menu, Category, Drink


class ProductsView(View):
    # Create
    def post(self, request):
        data = json.loads(request.body)
        menu = Menu.objects.create(name=data["menu"])
        category = Category.objects.create(name=data["category"], menu=menu)
        Drink.objects.create(name=data["product"], category=category, menu=menu)

        return JsonResponse({"messasge": "created"}, status=201)

    # Read
    def get(self, request):
        products = Drink.objects.all()
        results = []

        for product in products:
            results.append(
                {
                    "menu": product.category.menu.name,
                    "category": product.category.name,
                    "product_name": product.name,
                }
            )

        return JsonResponse({"results": results}, status=200)

