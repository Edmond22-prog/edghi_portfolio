from django.shortcuts import render

from website.models.biography import Biography
from website.models.resume import Resume, ResumeFile


def base(request):
    context = {}
    biography = Biography.objects.first()
    if biography:
        context["biography"] = biography
    
    resume = Resume.objects.filter(display=True).order_by("position")
    if resume:
        context["resume"] = resume
    
    resume_file = ResumeFile.objects.all().order_by("version").last()
    if resume_file:
        context["resume_file"] = resume_file.get_absolute_url()
        
    return render(request, "base.html", context)
