from rest_framework.decorators import api_view
from rest_framework.response import Response
from vendorsapp.serializers import *
from rest_framework import status

@api_view(['GET','POST'])
def all_vendors(request):
    if request.method == 'GET':
        vendors = Vendor.objects.all()
        serializers  = VendorSerializer(vendors, many=True)
        return Response(serializers.data)
    if request.method == 'POST':
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def edit_vendor(request,pk):
    try:
        vendor = Vendor.objects.get(pk=pk)
    except Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        vendor.delete()
        return Response('Deleted Successful', status=status.HTTP_204_NO_CONTENT)