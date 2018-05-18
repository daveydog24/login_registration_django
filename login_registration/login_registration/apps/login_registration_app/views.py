from django.shortcuts import render, redirect
from django.contrib import messages
from models import User
import bcrypt

def index(request):
    return render(request, 'login_registration_app_templates/index.html')

def registration(request):
    errors = User.objects.validate_user(request.POST)

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
            return redirect('/')

    messages.success(request, "you successfully registered!!!")
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    hash_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hash_password)
    user.save()
    request.session['id'] = user.id
    
    return redirect('/success')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
 
    get_user = User.objects.get(email=email)
    if (get_user):
        user_password = get_user.password
        check = bcrypt.checkpw(password.encode(), user_password.encode())
        if check == True:
            request.session['id'] = get_user.id
            messages.success(request, "you successfully logged in!!!")
            return redirect('/success')
        else:
            messages.error(request, "Email and password does not match our database.")
    return redirect('/')

def clear(request):
    request.session.clear()
    errors = {}
    return redirect('/')

def success(request):
    user_id = request.session['id']
    return render(request, 'login_registration_app_templates/success.html', {"user": User.objects.get(id=user_id)})

# Create your views here.
