from rest_framework import routers

from products.viewsets import ProductViewSet,ProductGenericViewSet

router = routers.DefaultRouter()

router.register(r'products', ProductGenericViewSet, basename='product')
print(router.urls)
urlpatterns = router.urls