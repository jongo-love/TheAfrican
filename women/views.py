from django.shortcuts import render

# Create your views here.
def home(request):
    # Render the home.html template
    return render(request, 'home.html')

def shop(request):
    return render(request, 'shop.html')

def categories(request):
    return render(request, 'categories.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')