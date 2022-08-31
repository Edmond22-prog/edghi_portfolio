from django.shortcuts import render
from django.views.generic import View

from website.models import Project, Resume, Cv


class HomeView(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        cv = Cv.objects.all().first()
        projects = Project.objects.all()
        communities = Resume.objects.filter(resume_type="Community").order_by("-id")
        professionals = Resume.objects.filter(resume_type="Professional").order_by("-id")
        context = {"projects": projects, "communities": communities, "professionals": professionals, "cv": cv}

        return render(request, self.template_name, context)
