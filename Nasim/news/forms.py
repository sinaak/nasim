from django import forms
from news.models import Contact


class Contacts(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name','phonenumber','email']
        
