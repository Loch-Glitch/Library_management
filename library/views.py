from django.shortcuts import render, redirect
from pymongo import MongoClient
from django.contrib import messages
from django.http import HttpResponse

client = MongoClient('mongodb://localhost:27017/')
db = client['Flipkart_user_data']
collection = db['Sign_up']
user_collection = db['user']

def index(request):
    return render(request, 'index.html')

def admin_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if collection.find_one({'username': username}) or collection.find_one({'email': email}):
            return HttpResponse("Username or email already exists.")

        elif password == password2:
            collection.insert_one({
                'username': username,
                'email': email,
                'password': password,
                'role': 'admin'
            })
            # return HttpResponse("Admin is successfully signed up!")
            return redirect('index')
        else:
            messages.error(request, 'Passwords do not match.')
    
    return render(request, 'adminsignup.html')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if user_collection.find_one({'username': username}) or user_collection.find_one({'email': email}):
           return HttpResponse("Username or email already exists.")
        elif password == password2:
            user_collection.insert_one({
                'username': username,
                'email': email,
                'password': password,
                'role': 'user'
            })
            # messages.success(request, 'User signed up successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Passwords do not match.')
    
    return render(request, 'usersignup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = user_collection.find_one({'username': username, 'password': password})
        if user:
            return redirect('selection')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'userlogin.html')

def selection_page(request):
    return render(request, 'selectionpage.html')

def user_selection(request):
    return render(request, 'userselection.html')

