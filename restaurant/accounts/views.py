from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm


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
                     

def login(request):
       pass
       # return render(request, 'accounts/login.html')
       