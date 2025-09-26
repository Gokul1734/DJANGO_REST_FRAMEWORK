from rest_framework import routers

from products.viewsets import ProductViewSet

router = routers.DefaultRouter()

router.register(r'products', ProductViewSet, basename='product')

urlpatterns = router.urls