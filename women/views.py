from django.shortcuts import render

# Create your views here.
def home(request):
    # Render the home.html template
    return render(request, 'home.html')