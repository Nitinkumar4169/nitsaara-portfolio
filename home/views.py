from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect

from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages



# Create your views here.
def index(request):
    context = {
        'variable1': " -> This is variable1 sent from views.py",
        'variable2': " -> This is variable2 sent from views.py" 
    }
    #messages.success(request, "This is a test message!")
    return render(request, 'index.html')
     #return HttpResponse("This is the home page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is the about page")

def services(request):  
    return render(request, 'services.html')
    #return HttpResponse("This is the services page")

# def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent successfully!")
    return render(request, 'contact.html')
    #return HttpResponse("This is the contact page")!



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        # Save to DB
        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            desc=desc
        )

        # Send Email to You
        subject = f"New Contact Message from {name}"
        message = f"""
Name: {name}
Email: {email}
Phone: {phone}

Message:
{desc}
        """

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ['nitinoffc2004@gmail.com'],
            fail_silently=False,
        )

        return redirect('contact')

    return render(request, 'contact.html')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        # Save to Database
        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            desc=desc
        )

        # Send Email Notification to You
        subject = f"New Contact Message from {name}"
        message = f"""
You have received a new message from your website:

Name: {name}
Email: {email}
Phone: {phone}

Message:
{desc}
        """

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ['nitinoffc2004@gmail.com'],  # your email
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent successfully!")

        return redirect('contact')  # Prevent duplicate submission

    return render(request, 'contact.html')    