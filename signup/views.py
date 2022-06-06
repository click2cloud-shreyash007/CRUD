

from django.shortcuts import redirect, render
from django.contrib.auth.models import User
# Create your views here.


def signup(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        # firstname = request.POST.get('first_name')
        # lastname = request.POST.get('last_name')
        # email = request.POST.get('email_id')
        # password = request.POST.get('password')
        
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email_id']
        password = request.POST['password']
        
       
        user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
        #user.save()
        print("user added successfully")
        return redirect('/login')
    else:
        return render(request, 'signup/signup_temp.html')
