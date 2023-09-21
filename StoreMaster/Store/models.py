from django.db import models

# Create your models here.
class Store(models.Model):
    store_id = models.AutoField(primary_key = True)
    store_name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 200)

    def get_store_id(self):
        return self.store_id

    def get_store_name(self):
        return self.store_name
    
    def get_address(self):
        return self.address
    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    store_id = models.ForeignKey(Store,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=150)
    product_description = models.CharField(max_length=1000)
    product_image = models.ImageField(null=True, blank=True,upload_to="images/")
    product_price = models.FloatField()
    product_location = models.CharField(max_length=10)
    product_stock = models.IntegerField()

    def get_name(self):
        return self.product_name
    
    def set_name(self, name):
        self.product_name = name

    def get_product_id(self):
        return self.product_id
    
    def get_store_id(self):
        return self.store_id
    
    def get_description(self):
        return self.product_description
    
    def set_description(self,description):
        self.product_description = description

    def get_price(self):
        return self.product_price
    
    #TODO add a sale option to this model to display as well
    def set_price(self,price):
        self.product_price = price

    def get_product_image(self):
        return self.product_image
    
    def set_product_image(self,image):
        self.product_image = image

    def get_product_location(self):
        return self.product_location
    
    def set_product_location(self,location):
        self.product_location = location

    def get_product_stock(self):
        return self.product_stock
    
    def set_product_stock(self, stock):
        self.product_stock = stock

    #TODO add verification for increase - make sure it doesn't go past a limit(could add a field for maximum stock?)
    def add_product_stock(self, increase):
        self.product_stock += increase

    #TODO add verification for remove - can't go past 0 
    def remove_product_stock(self, decrease):
        self.product_stock -= decrease
    

