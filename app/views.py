from django.shortcuts import render, redirect
from .models import Contact
from django.http import HttpResponse

def liste_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/liste.html', {'contacts': contacts})

def ajouter_contact(request):
    if request.method == "POST":
        nom = request.POST.get("nom")
        email = request.POST.get("email")
        telephone = request.POST.get("telephone")
        Contact.objects.create(nom=nom, email=email, telephone=telephone)
        return redirect('liste_contacts')
    return render(request, 'contacts/ajouter.html')

def supprimer_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return redirect('liste_contacts')
