from django.urls import path

from products.views import ProductsView

urlpatterns = [
    path("/drink", ProductsView.as_view()),
    # 어떤 뷰로 보낼지를 지정함
    # as_view는 프론트가 보낸 http 메서드와 view.py 메서드와 이름을 같게 한다.
]
# GET 127.0.0:8000/products
