from django.http import Http404
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CategorySerializer, ProductSerializer
from .models import Product, Category

class LatestProductsList(APIView):
    """
        List of Latest Registered Products
    """
    def get(self, request, format = None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)

class ProductDetail(APIView):

    def get(self, request, format = None, **kwargs):
        product = get_object_or_404(Product, slug=kwargs.get('product_slug'))
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryDetail(APIView):
    
    def get(self, request, format = None, **kwargs):
        category = get_object_or_404(Category, slug = kwargs.get('category_slug'))
        serializer = CategorySerializer(category)
        return Response(serializer.data)
