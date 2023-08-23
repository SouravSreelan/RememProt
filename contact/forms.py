from django.forms import ModelForm
from .models import Contacts

class ContactsForm(ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'





