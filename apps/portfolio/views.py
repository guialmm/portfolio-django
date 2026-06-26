from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Project, Skill
from .forms import ContactForm


def hub(request):
    project_count = Project.objects.count()
    skills_preview = Skill.objects.filter(category="lang").order_by("order")[:6]

    return render(request, "portfolio/hub.html", {
        "project_count": project_count,
        "skills_preview": skills_preview,
    })


def project_list(request):
    category = request.GET.get("cat", "")
    projects = Project.objects.all()
    if category:
        projects = projects.filter(category=category)

    categories = Project.CATEGORY_CHOICES

    return render(request, "portfolio/project_list.html", {
        "projects": projects,
        "categories": categories,
        "active_cat": category,
    })


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    all_projects = Project.objects.all()

    return render(request, "portfolio/project_detail.html", {
        "project": project,
        "all_projects": all_projects,
    })


def stack(request):
    active_cat = request.GET.get("cat", "")
    skills = Skill.objects.all()
    if active_cat:
        skills = skills.filter(category=active_cat)

    categories = Skill.CATEGORY_CHOICES
    skill_count = Skill.objects.count()

    return render(request, "portfolio/stack.html", {
        "skills": skills,
        "categories": categories,
        "active_cat": active_cat,
        "skill_count": skill_count,
    })


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem enviada com sucesso!")
            return redirect("contact")
    else:
        form = ContactForm()

    return render(request, "portfolio/contact.html", {"form": form})
