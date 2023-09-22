from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Store)
admin.site.register(User)
admin.site.register(Shipment)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Purchase)
