from rest_framework import generics

from products.models import Product
from products.serializers import productSerializer

class searchListView(generics.ListAPIView):
   queryset = Product.objects.all()
   serializer_class = productSerializer
   
   def get_queryset(self,*args,**kwargs):
      qs = super().get_queryset(*args,**kwargs)
      q = self.request.GET.get('q')
      user = None
      if self.request.user:
         user = self.request.user
      results = qs.filter(title__icontains=q)
      return user
   
