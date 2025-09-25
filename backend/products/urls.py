from django.urls import path

from . import views
from .views import product_detail_view

urlpatterns = [
   path('<int:pk>',product_detail_view,name='product-detail')
]
