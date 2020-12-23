from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100 , required=True)
    email = forms.EmailField(max_length=200, help_text='eg: example@gmail.com')
    
    class Meta :
        model = User
        fields =('username' , 'email' , 'password1' , 'password2')

class ContactForm(forms.ModelForm) :
    name = forms.CharField(max_length=100 , required=True , label="Name")
    email = forms.EmailField(max_length=200 , required=True , label="Email")
    subject = forms.CharField(max_length=100 , required=True , label="Subject")
    message = forms.Textarea()
    
    class Meta :
        model = Contact
        fields =('name' , 'email' , 'subject' , 'message')
        
    
    