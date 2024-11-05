from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item
from .serializers import ItemSerializer
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

# class ItemListView(ListCreateAPIView):
#     queryset = Item.object.all()
#     serializer_class = ItemSerializer
    
# class ItemDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Item.object.all()
#     serializer_class = ItemSerializer
#     lookup_field = 'id'

# @api_view(['GET', 'POST'])
# def item_list(request):
#     if request.method == 'GET':
#         items = Item.objects.all()
#         serializer = ItemSerializer(items, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = ItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def item_detail(request, id):
#     try:
#         item = Item.objects.get(pk=id)
#     except Item.DoesNotExist:
#         return Response(status=404)
    
#     if request.method == 'GET':
#         serializer = ItemSerializer(item)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = ItemSerializer(item, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         item.delete()
#         return Response(status=204)