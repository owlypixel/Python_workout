from django.conf.urls import url
from rest_framework import routers
from products.views import list_products, CategoriesList, ProductDetail, CategoryDetail, ProductViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = router.urls