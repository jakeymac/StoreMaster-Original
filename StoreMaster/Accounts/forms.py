from django import forms

#For validating and cleaning registration data
class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=35)
    last_name = forms.CharField(max_length = 50)
    email_address = forms.EmailField()
    #address = forms.CharField(max_length=200)
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    #other_information = forms.CharField(max_length = 1000,null=True,blank=True)
    #birthday = forms.DateField()


    #NEED TO MAKE THIS A DROP DOWN SELECTOR IN THE SITE
    #store_id = models.ForeignKey(Store,null=True,blank=True,on_delete=models.CASCADE)