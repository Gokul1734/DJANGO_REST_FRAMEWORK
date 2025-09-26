from rest_framework import viewsets 
from .models import Product
from .serializers import productSerializer

class ProductViewSet(viewsets.ModelViewSet):
   '''
      get -> list -> QuerySet
      get -> retrieve -> Product Instance Detail View
      post -> create -> Product Instance
      put -> update -> Product Instance
      patch -> partial_update -> Product Instance
      delete -> destroy -> Product Instance
   '''
   queryset = Product.objects.all()
   serializer_class = productSerializer
   lookup_field = 'pk'

class ProductGenericViewSet(viewsets.GenericViewSet, 
            viewsets.mixins.ListModelMixin,
            viewsets.mixins.RetrieveModelMixin,
            viewsets.mixins.CreateModelMixin,
            viewsets.mixins.UpdateModelMixin,
            viewsets.mixins.DestroyModelMixin):
   queryset = Product.objects.all()
   serializer_class = productSerializer
   lookup_field = 'pk'

product_list_view = ProductViewSet.as_view({'get': 'list'})
product_detail_view = ProductViewSet.as_view({'get': 'retrieve'})