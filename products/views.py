from rest_framework import viewsets
from .models import Category,Order,Product
from .serializers import CategorySerializer, OrderSerializer, ProductSerializer
from rest_framework.permissions import IsAdminUser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework import generics

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductListAPIView(generics.ListAPIView):  
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

@api_view(['GET'])
@swagger_auto_schema(
    operation_description="Retrieve a list of users",
    responses={200: 'List of users'},
)
def user_list(request):
    # Your view code here
    pass