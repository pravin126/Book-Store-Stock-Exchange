from django import forms
from books.models import Contact

class SaveConatct(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','address','phone','email','contact_type']
