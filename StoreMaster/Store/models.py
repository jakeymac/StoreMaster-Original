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
    
    def set_address(self, address):
        self.address = address

class User(models.Model):
    user_id = models.Autofield(primary_key=True)
    user_type = models.CharField(max_length=25)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length = 50)
    email_address = models.CharField(max_length = 75, null=True, blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    store_id = models.ForeignKey(Store,null=True,blank=True)
    username = models.CharField(max_length=30,null=True,blank=True)
    password = models.CharField(max_length=30,null=True,blank=True)
    other_information = models.CharField(max_length = 1000,null=True,blank=True)
    birthday = models.DateField(null=True,blank=True)
    
    def get_user_type(self):
        return self.user_type
    
    def set_user_type(self, type):
        self.user_type = type

    def get_first_name(self):
        return self.first_name
    
    def set_first_name(self, name):
        self.first_name = name

    def get_last_name(self):
        return self.last_name
    
    def set_last_name(self, name):
        self.last_name = name

    def get_email(self):
        return self.email_address
    
    def set_email(self, email):
        self.email_address = email
    
    def get_address(self):
        return self.address
    
    def set_address(self, address):
        self.address = address

    def get_store_id(self):
        return self.store_id
    
    def set_store_id(self, store):
        self.store_id = store

    def get_username(self):
        return self.username
    
    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_other_information(self):
        return self.other_information
    
    def set_other_information(self,info):
        self.other_information = info

    def get_birthday(self):
        return self.birthday
    
    def set_birthday(self, birthday):
        self.birthday = birthday

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
    
class Shipment(models.Model):
    shipment_id = models.AutoField(primary_key = True)
    shipment_origin = models.CharField(max_length = 70)
    destination_store_id = models.ForeignKey(Store,on_delete=models.CASCADE)
    expected_date = models.DateField()
    shipment_status = models.CharField(max_length=150)
    shipment_tracking_history = models.CharField(max_length=1000)
    shipment_tracking_link = models.CharField(max_length=100,null=True,blank=True)

    def get_shipment_id(self):
        return self.shipment_id
    
    def get_shipment_origin(self):
        return self.shipment_origin
    
    def set_shipment_origin(self, origin):
        self.shipment_origin = origin

    def get_destination_store_id(self):
        return self.destination_store_id
    
    def set_destination_store_id(self, store):
        self.destination_store_id = store

    def get_expected_date(self):
        return self.expected_date

    def set_expected_date(self, date):
        self.expected_date = date

    def get_shipment_status(self):
        return self.shipment_status
    
    def set_shipment_status(self, status):
        self.shipment_status = status

    def get_shipment_tracking_history(self):
        return self.shipment_tracking_history
    
    def set_shipment_tracking_history(self,history):
        self.shipment_tracking_history = history

    def get_tracking_link(self):
        return self.shipment_tracking_link
    
    def set_tracking_link(self,link):
        self.shipment_tracking_link = link

#Could add location to track the register/location the purchase was made
class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key = True)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User,on_delete=models.CASCADE)
    purchase_date = models.DateTimeField()
    purchase_total = models.FloatField() #could update this model for tax registration
    items = models.CharField(max_length=800)

    def get_purchase_id(self):
        return self.purchase_id

    def get_store_id(self):
        return self.store_id
    
    def set_store_id(self, store):
        self.store_id = store

    def get_employee_id(self):
        return self.employee_id
    
    def set_employee_id(self, employee):
        self.employee_id = employee

    def get_customer_id(self):
        return self.customer_id
    
    def set_customer_id(self,customer):
        self.customer_id = customer 

    def get_purchase_date(self):
        return self.purchase_date
    
    def set_purchase_date(self, date):
        self.purchase_date = date

    def get_total(self):
        return self.purchase_total
    
    def set_total(self, total):
        self.purchase_total = total

    def get_items(self):
        return self.items
    
    def set_items(self, items):
        self.items = items

class Order(models.Model):
    order_id = models.AutoField(primary_key = True)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User,on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    destination = models.CharField(max_lenght = 100, null = True, blank = True)
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