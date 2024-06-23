from rest_framework import status
from rest_framework.response import Response 
# from rest_framework.decorators import api_view

from manytoManyExample.models  import Customer, Product, Order
from manytoManyExample.api.serializers import CustomerSerializer, ProductsSerializer, OrderSerializer

#class views
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404



class CustomersListCreateAPIView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True, context={'request': request}) 
        return Response(serializer.data)


    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductsListCreateAPIView(APIView):
    def get(self, request):
        products = Product.objects.all() 
        serializer = ProductsSerializer(products, many=True, context={'request': request}) 
        return Response(serializer.data)


    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrdersListCreateAPIView(APIView):
    def get(self, request):
        products = Order.objects.all() 
        serializer = OrderSerializer(products, many=True, context={'request': request}) 
        return Response(serializer.data)


    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class MakaleDetailAPIView(APIView):

#     def get_object(self, pk):
#         makale_instance = get_object_or_404(Makale, pk=pk)
#         return makale_instance

#     def get(self, request, pk):
#         makale = self.get_object(pk=pk)
#         serializer = MakaleSerializer(makale) 
#         return Response(serializer.data)       

#     def put(self, request, pk):
#         makale = self.get_object(pk=pk)
#         serializer = MakaleSerializer(makale, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      

#     def delete(self, request, pk):
#         makale = self.get_object(pk=pk)
#         makale.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)