# import json

# from django.http import JsonResponse  # json으로 응답할 수 있도록
# from django.views import View

# from products.models import Menu, Category, Drink


# class ProductsView(View):
#     def post(self, request):
#         data = json.loads(request.body)  # JSON => dictionary
#         menu = Menu.objects.create(name=data["name"])
#         category = Category.objects.create(
#             name=data["category"], menu=menu
#         )  # menu_id = menu.id

#         Drink.objects.create(
#             korean_name=data["product"],
#             category=category,
#             # menu=menu,
#             # description="I love you",
#             # english_name="a",
#         )
#         return JsonResponse({"MESSAGE": "CREATED"}, status=201)

#     # Read
#     def get(self, request):  # 프론트가 request로 주었던 것을 가지고 행동
#         products = Drink.objects.all()  # 쿼리셋을 products에 담음, for문을 돌릴 수 있다.
#         results = []
#         for product in products:
#             results.append(
#                 {
#                     "menu": product.category.menu.name,
#                     "category": product.category.name,
#                     "product_name": product.korean_name,
#                 }
#             )

#         return JsonResponse({"results": results}, status=200)
import json

from django.http import JsonResponse  # json으로 응답할 수 있도록
from django.views import View

from products.models import Menu, Category, Drink


class ProductsView(View):
    def post(self, request):
        data = json.loads(request.body)  # JSON => dictionary
        menu = Menu.objects.create(name=data["menu"])
        category = Category.objects.create(
            name=data["category"], menu=menu, menu_id=menu.id,
        )
        Drink.objects.create(
            korean_name=data["korean_name"], category=category,
        )
        return JsonResponse({"MESSAGE": "CREATED"}, status=201)

    # Read
    def get(self, request):  # 프론트가 request로 주었던 것을 가지고 행동
        products = Drink.objects.all()  # 쿼리셋을 products에 담음, for문을 돌릴 수 있다.
        results = []
        for product in products:
            results.append(
                {
                    "menu": product.category.menu.name,
                    "category": product.category.name,
                    "product_name": product.korean_name,
                }
            )

        return JsonResponse({"results": results}, status=200)
