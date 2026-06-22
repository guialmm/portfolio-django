from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill
from .forms import ContactForm


def home(request):
    projects = Project.objects.all()
    featured = projects.filter(is_featured=True)
    skills = Skill.objects.all()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem enviada! Responderei em breve.")
            return redirect("home")
    else:
        form = ContactForm()

    return render(request, "portfolio/home.html", {
        "projects": projects,
        "featured": featured,
        "skills": skills,
        "form": form,
    })
