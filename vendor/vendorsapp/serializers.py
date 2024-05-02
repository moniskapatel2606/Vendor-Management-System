from rest_framework import serializers
from .models import *

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
class PurchaseOrderSerializer(serializers.ModelSerializer):
    vendor=VendorSerializer(many=True)
    class Meta:
        model=PurchaseOrder
        fields='__all__'