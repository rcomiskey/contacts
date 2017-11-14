from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import UserLoginForm

def get_index(request):
   return render(request, "index.html")
   
def logout(request):
    auth.logout(request)
    return render(request, "index.html")
    
def login(request):
    if request.method=="POST":
        form=UserLoginForm(request.POST)
        
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])

            if user is not None:
                auth.login(request, user)
                
            return redirect(get_index)
        
    else:
        form = UserLoginForm()
    
    return render(request, "login.html", {'form': form})