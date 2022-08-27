from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        ...
