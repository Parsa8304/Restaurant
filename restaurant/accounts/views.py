from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm
from vendor.forms import VendorForm
from django.contrib.auth.models import User


def register(request):
       
       if request.method == 'POST':
              form = UserForm(request.POST)
              if form.is_valid():
                     form.save()
                     messages.success(request, 'Account created successfully!')
                     return redirect('accounts:login')
              else:
                     messages.error(request, 'Invalid Credentials!')
       else:
              form = UserForm()
       return render(request, 'accounts/register.html', {'form': form})
                     
                     
def register_vendor(request):
       if request.method == 'POST':
              form = VendorForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        
              if form.is_valid():            
                   user = User.objects.create_user(
                   username=form.cleaned_data['username'],
                   email=form.cleaned_data['email'],
                   password=form.cleaned_data['password']
            )
                   user.is_vendor = True  
                   user.save()
            
        
                   vendor = form.save(commit=False)
                   vendor.user = user
                   vendor.save()
            
                   messages.success(request, 'Vendor account created successfully!')
                   return redirect('accounts:login')
              else:
                     messages.error(request, 'Please correct the errors below.')
       else:
              form = VendorForm()
    
       return render(request, 'accounts/register_vendor.html', {'form': form})
       
       
       
       
       
       
def login(request):
       pass
       # return render(request, 'accounts/login.html')
       