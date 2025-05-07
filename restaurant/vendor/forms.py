from django import forms
from .models import Vendor



class VendorForm(forms.ModelForm):
       username = forms.CharField(max_length=150, label='Username')
       email = forms.EmailField(label='Email')
       password = forms.CharField(widget=forms.PasswordInput, label='Password')
       confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
       
       
       class Meta:
              model = Vendor
              fields = ['vendor_name', 'vendor_liecense',  'username', 'email', 'password', 'confirm_password']
              
       def clean(self):
              cleaned_data = super().clean()
              password = cleaned_data.get('password')
              confirm_password = cleaned_data.get('confirm_password')
              
              if password and confirm_password and password != confirm_password:
                     raise forms.ValidationError("Passwords do not match")
              return cleaned_data