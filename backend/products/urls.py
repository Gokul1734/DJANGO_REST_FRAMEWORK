from django.urls import path

from . import views
from .views import product_alt_view

urlpatterns = [
   path('',views.product_alt_view),
   path('<int:pk>',views.product_alt_view)
]
