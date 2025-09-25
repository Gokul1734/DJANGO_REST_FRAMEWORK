from rest_framework import generics

from .models import Product
from .serializers import productSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
   queryset = Product.objects.all()
   serializer_class = productSerializer

product_detail_view = ProductDetailAPIView.as_view()