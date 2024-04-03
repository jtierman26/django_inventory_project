#parts of this code were obtained and modified to the programs needs from 
#[1]“Build an Inventory Management System with Python and Django - Overview,” 
#www.youtube.com. https://www.youtube.com/watch?v=axGWgK2ep4Q&list=PLWwo7xJYACuQ2tVSIzAarcUvNlR3oTk-w&index=1 (accessed Mar. 30, 2024). 

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

#function to login the user 
def login_employee(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

    #authentication check
        user = authenticate(request, username= username, password= password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'Oops! Something went wrong! ' )
            return redirect('login')
    else:
        return render(request, 'users/login.html')


#function to logout user
def logout_employee(request):
    logout(request)
    messages.info(request, 'You have been logged out. Please sign in to continue ')
    return redirect('login')