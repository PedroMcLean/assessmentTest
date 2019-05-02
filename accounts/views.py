from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

#Validating if the user has completed the signup form correctly
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('clients:list')
    else:
        form = UserCreationForm()
    return render (request, 'accounts/signup.html', {'form':form})

#Validating the users credentials, and then logging the user in
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log user in
            user = form.get_user()
            login(request, user)
            return redirect('clients:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

#Logging the user out of the system
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')
