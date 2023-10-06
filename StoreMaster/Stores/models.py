from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Store(models.Model):
    store_id = models.AutoField(primary_key = True)
    store_name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 20)
    zip_code = models.IntegerField()

    def __str__(self):
        return f"{self.store_name} - {self.address}, {self.city}, {self.state}"

    def get_store_id(self):
        return self.store_id

    def get_store_name(self):
        return self.store_name
    
    def get_address(self):
        return self.address
    
    def set_address(self, address):
        self.address = address