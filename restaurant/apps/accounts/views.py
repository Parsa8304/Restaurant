from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm
from apps.vendor.forms import VendorForm
from .models import User, UserProfile
from django.db import IntegrityError


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
              form = VendorForm(request.POST, request.FILES)  
        
              if form.is_valid():            
                     if User.objects.filter(username=form.cleaned_data['username']).exists:
                            messages.error(request, 'Username already exists.')
                            return redirect('accounts:registervendor')
                   
                     try:
                            user = User.objects.create_user(
                                   username=form.cleaned_data['username'],
                                   email=form.cleaned_data['email'],
                                   password=form.cleaned_data['password']
                     )
                            user.is_vendor = True  
                            user.save()
                            user_profile, created= UserProfile.objects.get_or_create(user=user)
                            
                            vendor = form.save(commit=False)
                            vendor.user = user
                            vendor.user_profile = user_profile
                            vendor.save()
                            
                            messages.success(request, 'Vendor account created successfully!')
                            return redirect('accounts:login')
                   
                     except IntegrityError:
                            messages.error(request, 'An error occurred while creating the vendor account. Please try again.')
                            return redirect('accounts:register_vendor')
                     
                     except Exception as e:
                            messages.error(request, f'Unexpected error: {str(e)}')
                            return redirect('accounts:register_vendor')
                            
              else:
                     messages.error(request, 'Please correct the errors below.')           
                                 
       else:
              form = VendorForm()
    
       return render(request, 'accounts/register_vendor.html', {'form': form})
             
       
# def login(request):
#        return render(request, 'accounts/login.html')
def login(request):
       return render(request, 'accounts/login.html')

       
       
def logout(request):
       pass

def dashboard(request):
       pass       


