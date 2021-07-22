from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from interviewers.models import Companies

class SignupForm(UserCreationForm):
    email = forms.CharField(required=True,widget=forms.EmailInput,max_length=255)
    username = forms.CharField(required=True,max_length=100, label='Username', widget=forms.TextInput)
    first_name = forms.CharField(label='First Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

class NewCompanyForm(forms.ModelForm):
    name = forms.CharField(required=True,label="Company Name",max_length=100)
    website = forms.CharField(required=True,label="Website Name",max_length=100, initial="https://")
    phoneNo = forms.IntegerField(required=True,label="Phone Number")
    class Meta:
        model = Companies
        fields = ['name','website','phoneNo']

