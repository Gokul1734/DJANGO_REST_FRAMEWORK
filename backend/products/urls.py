from django.urls import path

from . import views
from .views import ProductMixinView, product_list_create_view,product_create_view

urlpatterns = [
   path('',views.product_list_create_view),
   path('<int:pk>',views.product_list_create_view),
   path('<int:pk>/update',views.ProductMixinView),
   path('<int:pk>/delete',views.ProductMixinView),
   path('create',views.product_create_view),
]
