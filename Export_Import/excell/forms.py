from django import forms
from .models import home

class Studentregi(forms.ModelForm):
    class Meta:
        model=home
        fields=['s_no','first_name','last_name','email']
        widgets={
        's_no':forms.TextInput(attrs={"class":"form-control"}),
        'first_name':forms.TextInput(attrs={"class":"form-control"}),
        'last_name':forms.TextInput(attrs={"class":"form-control"}),
        'email':forms.EmailInput(attrs={"class":"form-control"})
        }