import random

from django.shortcuts import render
from rest_framework import viewsets, status
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView


#Postman tarafından statuslar felan cok net gozkuuyor
class ProductViewSet(viewsets.ViewSet):

    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


    #POSTMAN body raw json {"title":"title, ...
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    #127.0.0.1:8000/api/products/1
    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


    #Put 127.0.0.1:8000/api/products/1
    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


    #Delete
    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#127.0.0.1:8000/api/user
class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choices(users)
        return Response({
            'id': user.id
        })