from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

class productSerializer(serializers.ModelSerializer):
   url = serializers.SerializerMethodField(read_only=True)
   email = serializers.EmailField(write_only=True)

   class Meta:
      model = Product
      fields = [
         'user',
         'url',
         'pk',
         "title",
         "email",
         "content",
         "price",
         "sale_price"
      ]
   
   def get_url(self,obj):
      request = self.context.get('request')
      if request is None:
         return None
      return reverse("product-detail",kwargs={"pk":obj.pk},request=request)
   def get_discount(self,obj):
      try:
         return obj.get_discount()
      except:
         return None