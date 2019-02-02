from django import forms

from.models import contact

class ContactForm(forms.ModelForm):
    class meta:
        model = contact
        fields = ('first_name','last_name','email', 'message')


        