# views.py
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Receipe  # Make sure your model name is correct

def index(request):
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
            return redirect('/show.html')
      
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
    return redirect('/show.html')

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
     