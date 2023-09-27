from django.db import models
from Stores.models import Store
from Accounts.models import CustomerInfo
# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key = True)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(CustomerInfo,on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    destination = models.CharField(max_length = 100, null = True, blank = True)
    order_total = models.FloatField()
    items = models.CharField(max_length = 800)

    def get_order_id(self):
        return self.order_id
    
    def get_store_id(self):
        return self.store_id
    
    def set_store_id(self, store):
        self.store_id = store

    def get_customer_id(self):
        return self.customer_id
    
    def set_customer_id(self,customer):
        self.customer_id = customer 

    def get_order_date(self):
        return self.order_date
    
    def set_order_date(self,date):
        self.order_date = date

    def get_destination(self):
        return self.destination
    
    def set_destination(self, destination):
        self.destination = destination

    def get_order_total(self):
        return self.order_total
    
    def set_order_total(self, total):
        self.order_total = total

    def get_items(self):
        return self.items
    
    def set_items(self, items):
        self.items = items