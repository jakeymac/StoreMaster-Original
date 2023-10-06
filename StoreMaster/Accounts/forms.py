from django import forms
from django.forms.widgets import DateInput
from Stores.models import Store


#For validating and cleaning registration data
class RegistrationForm(forms.Form):
    first_name = forms.CharField(required=True,label="First Name",max_length=35)
    last_name = forms.CharField(required=True,label="Last Name",max_length=50)
    email_address = forms.EmailField(required=True,label="Email Address")
    address = forms.CharField(required=False,label="Address",max_length=200)
    username = forms.CharField(required=True,label="Username",max_length=30)
    password = forms.CharField(required=True, widget=forms.PasswordInput,label="Password",max_length=30)
    other_information = forms.CharField(required=False,label="Other Information",max_length = 1000)

    birthday = forms.DateField(required=False,label="Birthday")
    birthday = forms.DateField(widget=DateInput(attrs={'type':'date'}))
    
    choices = [(store.store_id, store.store_name) for store in Store.objects.all()]
    choices.insert(0, ('', 'Select Store'))
    store_id = forms.ChoiceField(required=False,label="Store Location", choices=choices)

    user_types = [("employee","Employee"), ("manager","Manager"),("admin","Admin")]
    user_type = forms.ChoiceField(required=True,label="Account Type", choices = user_types,)



    #NEED TO MAKE THIS A DROP DOWN SELECTOR IN THE SITE
    #store_id = models.ForeignKey(Store,null=True,blank=True,on_delete=models.CASCADE)

    """ <label for="first_name">First Name:</label>
        <input type="text" id="first_name" name="first_name" required><br><br>

        <label for="last_name">Last Name:</label>
        <input type="text" id="last_name" name="last_name" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>

        <label for="store_selector">Store:</label>
        <select id="store_selector" name="store_selector">
            {% for store in stores %}
                <option value="{{store}}">{{store}}</option>
            {% endfor %}
        </select><br><br>


        <label for="user_type_selector">User Type:</label>
        <select id="user_type_selector" name="user_type_selector">
            <option value ="admin">Admin</option>
            <option value="manager">Manager</option>
            <option vlaue="employee" selected>Employee</option>
        </select><br><br>
"""