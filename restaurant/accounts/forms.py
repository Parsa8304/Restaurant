from django import forms
from django.core.exceptions import ValidationError
from .models import User


class UserForm(forms.ModelForm):
       password = forms.CharField(widget=forms.PasswordInput, label='Password')
       confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
       
       def clean_email(self):
              email = self.cleaned_data.get('email')
              if User.objects.filter(email=email).exists():
                     raise forms.ValidationError("Email already exists")
              return email
       
       
       
       
       
       def clean(self):
              cleaned_data = super().clean()
              password = cleaned_data.get("password")
              confirm_password = cleaned_data.get("confirm_password")
              
              if password and confirm_password and password != confirm_password:
                     raise forms.ValidationError("Passwords do not match")
              
              return cleaned_data
       class Meta:
              model = User
              fields = ['first_name', 'last_name','username', 'email', 'phone_number', 'password', 'confirm_password']
              
              