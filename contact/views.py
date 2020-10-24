from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.urls import reverse

# Create your views here.

def contact(request):
    print("tipo de metodo de envio {}", request.method)
    contactform = ContactForm()
    if request.method == "POST":
        contactform = ContactForm(data=request.POST)
        if contactform.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
        #enviamos el correo
        email = EmailMessage(
            "La cafettiera",
            "De {} <{}>\n\n{}".format(name, email, content),
            "no contestar",
            ["jafalcones@est.itsgg.edu.ec"],
            reply_to= [email]
        )
        try:
            email.send()
            return redirect(reverse('contact')+"?ok")
        except:
            return redirect(reverse('contact')+"?fail")
    
    return render(request, 'contact/contact.html', {'form': contactform})
