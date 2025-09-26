from rest_framework import generics, permissions
from .models import Product
from .serializers import productSerializer


class ProductCreateAPIVIew(generics.CreateAPIView):
   queryset = Product.objects.all()
   serializer_class = productSerializer
   permission_classes = [permissions.IsAuthenticated]
   
   def perform_create(self, serializer):
      print(serializer.validated_data)
      title = serializer.validated_data.get('title')
      content = serializer.validated_data.get('content') or None
      if content is None:
         content = title
      serializer.save(content=content)