from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact, Project, Skill
from .forms import ContactForm

def home(request):
    #Exibe a landing page com os projetos
    projects = Project.objects.all()
    skills = Skill.objects.all()
    context = {
        'skills': skills,
    }
    return render(request, 'portfolio_app/home.html', {'projects': projects, 'skills': skills})
   

def contact_create(request):
    #View para criar um novo contato(CRUD)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contato enviado com sucesso!')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'portfolio_app/contact_create.html', {'form': form})
