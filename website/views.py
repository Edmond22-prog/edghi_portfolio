from django.shortcuts import render
from django.views.generic import View

from website.models import Project, Resume


class HomeView(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        communities = Resume.objects.filter(resume_type="Community").order_by("-id")
        professionals = Resume.objects.filter(resume_type="Professional").order_by("-id")
        context = {"projects": projects, "communities": communities, "professionals": professionals}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        ...
