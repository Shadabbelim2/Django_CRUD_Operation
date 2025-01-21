# views.py
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Receipe  # Make sure your model name is correct
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    if request.user.is_anonymous:
        return redirect("/login-page")
   
    if request.method == "POST":
        receipe_name = request.POST.get('recipeName')  # Name should match your form field
        receipe_description = request.POST.get('recipeDescription')
        receipe_image = request.FILES.get('recipeImage')  # File upload ke liye
        
        if receipe_name and receipe_description and receipe_image:
            # Save data to the database
            Receipe.objects.create(
                receipe_name=receipe_name,
                receipe_description=receipe_description,
                receipe_image=receipe_image
            )
            return redirect('show')
      
    return render(request, 'index.html')

def show(request):
    Receipese=Receipe.objects.all()
    
    if request.GET.get('search'): 
        Receipese=Receipese.filter(receipe_name__icontains = request.GET.get('search'))
    context={"Receipes" : Receipese}
    return render(request , 'show.html' , context )

def delete_receipe(request , id):
    quereset=Receipe.objects.get(id=id)
    quereset.delete()
    return redirect('show')

def update_receipe(request , id):
    queryset=Receipe.objects.get(id = id)
    if request.method == "POST":
        receipe_name = request.POST.get('recipeName')  # Name should match your form field
        receipe_description = request.POST.get('recipeDescription')
        receipe_image = request.FILES.get('recipeImage')  # File upload ke liyeif

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        if receipe_image:
            queryset.receipe_image=receipe_image
        queryset.save()
        return redirect('/show.html')
    context={'receipe':queryset}
    return render(request , 'update.html' , context )
     
def ragister(request):
    if request.method =="POST":
        username=request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request, "Username already Exists Plese Login in")

            return redirect('ragister')

        user=User(username=username , email = email )
        user.save()
        user.set_password(password)
        user.save()
        messages.success(request, "Ragister successfull Plese login.")

        return redirect('ragister')

    return render(request , 'ragister.html')  

def login_page(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username , password)
        if not User.objects.filter(username = username).exists():
            messages.error(request, "User Not Ragister.")
            return redirect('login_page')
        user = authenticate(request, username=username , password=password)
        if user is not None:
             login(request, user)
             return redirect('/') 
            
        else:
            messages.error(request, "Invalid Crudntioals.")
            return redirect('login_page')
               
    return render(request , 'login_page.html')      

def logout_page(request):
    logout(request)
    return redirect('login_page')  