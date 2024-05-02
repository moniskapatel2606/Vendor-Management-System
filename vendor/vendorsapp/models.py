from django.db import models


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
    

#Backend Logic
# @receiver(post_save, sender=PurchaseOrder)
# def calculate_on_time_delivery_rate(sender, instance, created, **kwargs):
#     if instance.status == 'completed':
#         # Logic to calculate on-time delivery rate...

# @receiver(post_save, sender=PurchaseOrder)
# def update_quality_rating_average(sender, instance, created, **kwargs):
#     if instance.quality_rating is not None:
#         # Logic to update quality rating average...

# @receiver(post_save, sender=PurchaseOrder)
# def calculate_average_response_time(sender, instance, created, **kwargs):
#     if instance.acknowledgment_date:
#         # Logic to calculate average response time...

# @receiver(post_save, sender=PurchaseOrder)
# def calculate_fulfillment_rate(sender, instance, created, **kwargs):