from django.shortcuts import redirect, render
from django.contrib import auth

# Create your views here.
def login(request):
    y = False
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        
        x = auth.authenticate(username=username, password=password)
        if x is None:
            y = True
            return redirect('login')
            
        else:
            return render(request,"shop/item_list.html")
        
        
    else:
        return render(request, 'login/login_temp.html')