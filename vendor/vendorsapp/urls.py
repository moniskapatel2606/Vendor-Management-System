from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('',index),
    path('api/vendors/', VendorListCreateAPIView.as_view(), name='vendor-list'),
    path('api/vendors/<int:pk>/', VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor-detail'),
    path('api/purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchaseorder-list'),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchaseorder-detail'),
    path('api/vendors/<int:pk>/performance/', VendorPerformanceAPIView.as_view(), name='vendor-performance'),
    path('api/purchase_orders/<int:pk>/acknowledge/', AcknowledgePurchaseOrderAPIView.as_view(), name='acknowledge-purchaseorder'),
]