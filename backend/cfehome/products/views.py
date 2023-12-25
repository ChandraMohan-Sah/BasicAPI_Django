'''
The serializer_class attribute is a way to tell DRF how to 
convert complex data types, such as Django models, into formats 
that can be easily rendered into JSON responses or parsed from 
incoming JSON requests. It plays a crucial role in the serialization 
and deserialization process within DRF.
'''

from rest_framework import generics, authentication, permissions
from .models import Product
from .serializers import ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None :
            content = title 
        serializer.save(content = content)

#short func name for urls.py
product_create_view = ProductCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    # Product.objects.get(pk =1 )

product_detail_view = ProductDetailAPIView.as_view()


class ProductListAPIVIew(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
product_list_view = ProductListAPIVIew.as_view()


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None :
            content = title 
        serializer.save(content = content)

#short func name for urls.py
product_list_create_view = ProductListCreateAPIView.as_view()



'''--------------------------->
Next Step : Look at the 
views that does both of things:
    updating smthg
    deleting smthg

    PUT -> update 
    DESTROY ->delete

    Simliary Approach to RetrieveAPIView
'''

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    # Product.objects.get(pk =1 )

    def perform_update(self, serializer):
        # return super().perform_update(serializer)
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title 

product_update_view = ProductUpdateAPIView.as_view()



class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    # Product.objects.get(pk =1 )

    def perform_destroy(self, instance):
        #instance 
        super().perform_destroy(instance)

product_delete_view = ProductDestroyAPIView.as_view()


