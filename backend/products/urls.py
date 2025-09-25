from django.urls import path

from . import views
from .views import ProductMixinView

urlpatterns = [
   path('',views.ProductMixinView),
   path('<int:pk>',views.ProductMixinView)
]
