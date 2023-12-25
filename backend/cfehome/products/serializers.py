from  rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Product 
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()

'''

When DRF encounters a serializer field with a name like my_discount 
and sees that there's a method named get_my_discount, it automatically 
calls this method to calculate the value for the my_discount field when
serializing the object.

In your serializer, you don't explicitly call get_my_discount yourself. 
Instead, DRF takes care of calling it during the serialization process. 
The framework follows conventions, and as long as you adhere to these 
conventions, it will automatically use the appropriate methods for calculating 
custom field values.

'''