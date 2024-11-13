from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def home(request):
    # Render the home.html template
    return render(request, 'home.html')

def shop(request):
    return render(request, 'shop.html')

def categories(request):
    return render(request, 'categories.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data, e.g., send an email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Send an email (make sure to configure your email settings in settings.py)
            try:
                send_mail(
                    subject,
                    message,
                    email,
                    [settings.CONTACT_EMAIL],  # Set CONTACT_EMAIL in settings.py
                    fail_silently=False,
                )

                # Display a success message
                messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            except Exception as e:
                # Handle sending email failure
                messages.error(request, 'Oops! Something went wrong, please try again later.')

            # Redirect to the contact page or any other page after submission
            return render(request, 'contact.html', {'form': form})

    else:
        form = ContactForm()
    return render(request, 'contact.html',{'form': form})

def about(request):
    return render(request, 'about.html')