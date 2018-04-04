from django import forms
from allinone.models import Contact,Feedbacksuggestions


class Contacts(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name','phonenumber','email']
        

class Feedbacksuggestion(forms.ModelForm):

    class Meta:
        model = Feedbacksuggestions
        fields = ['name','email','comment']
        