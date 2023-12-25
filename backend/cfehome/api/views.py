from products.models import Product
from django.http import JsonResponse

#rest_framework views and responces
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


# Design Our First API 
@api_view(["GET"])
def api_home_get(request, *args, **kwargs):
    '''DRF API View'''

    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
    return Response(data)



@api_view(['POST'])
def api_home_post(request, *args, **kwargs):
    '''DRF API View'''

    # Validate the posted data using serializer
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True): 
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)
    return Response({"invalid":"not good data "}, status=400)


'''
If serializer.is_valid(raise_exception=True): 
    Implies ..If a valid data is not sent ...It raise exceptions

Like :
1) {"title": " "}
        {'title': ['This field may not be blank.']}

2) {"price": "abc123"}:then message is :
         {'price': ['A valid number is required.']}
'''



'''
Data that is comming through is checked ,does it matchs with  requirements of 
serializer.

Then, Second the requirements of the model. In this case the 
requirements of the model are  :
    title:([Aru field ma Null Paenxa])

'''