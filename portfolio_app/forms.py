from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    #Formulário para o model Contact
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'message']

        