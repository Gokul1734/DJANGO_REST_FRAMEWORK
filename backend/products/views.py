from rest_framework import generics

from .models import Product
from .serializers import productSerializer

from rest_framework.decorator import api_view
from rest_framework.response import Response


from django.shortcuts import get_object_or_404 

class ProductCreateAPIVIew(generics.CreateAPIView):
   queryset = Product.objects.all()
   serializer_class = productSerializer
   
   def perform_create(self, serializer):
      print(serializer.validated_data)
      title = serializer.validated_data.get('title')
      content = serializer.validated_data.get('content') or None
      if content is None:
         content = title
      serializer.save(content=content)

class ProductDetailAPIView(generics.RetrieveAPIView):
   queryset = Product.objects.all()
   serializer_class = productSerializer

class ProductListCreateAPIVIew(generics.ListCreateAPIView):
   queryset = Product.objects.all()
   serializer_class = productSerializer
   
   def perform_create(self, serializer):
      print(serializer.validated_data)
      title = serializer.validated_data.get('title')
      content = serializer.validated_data.get('content') or None
      if content is None:
         content = title
      serializer.save(content=content)
   
product_list_create_view = ProductListCreateAPIVIew.as_view()

product_create_view = ProductCreateAPIVIew.as_view()

product_detail_view = ProductDetailAPIView.as_view()

@api_view(['GET','POST'])
class product_alt_view(request,pk=None,*args,**kwargs):
   
   if method == 'GET':
      
      if pk is not None:
         queryset = Product.objects.filter(pk=pk)
         obj = get_object_or_404(Product,pk=pk)
         data = productSerializer(querySet,many=False).data
         return Response(data)
      
      querySet = Product.objects.all()
      data = productSerializer(querySet,many=True).data
      return Response(data)
   
   if method == 'POST':
      serializer = productSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
         title = serializer.validated_data.get('title')
         content = serializer.validated_data.get('content') or None
         if content is None:
            content = title
         serializer.save(content=content)
         return Response(serializer.data)
   