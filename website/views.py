from django.shortcuts import render, redirect, get_object_or_404
from django.utils.html import format_html
from django.contrib import messages
from django.views.generic import View, TemplateView
from datetime import date
from .forms import TestimonialForm
from .models import AboutInfo, Count, Interest, Testimonial, Project, ProjectImage

# Your views here

# Function to calculate age
def calculate_age(birth_date: date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

class HomeView(View):
    template_name = 'index.html'
    initial = {'key': 'value'}
    form_class = TestimonialForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        
        # Query DB data
        about = AboutInfo.objects.first()
        counts = Count.objects.all()
        interest = Interest.objects.all()
        testimonials = Testimonial.objects.all()
        testimonials_count = Testimonial.objects.filter(show=True)
        projects = Project.objects.all()
        images = []
        
        # Filter images for each of the projects and append to images list.
        for project in projects:
            project_images = ProjectImage.objects.filter(project=project)
            images.append(project_images)
           
        context = {
            'age': calculate_age(date(1999, 5, 22)),
            'form': form,
            'about': about,
            'counts': counts,
            'interests': interest,
            'testimonials': testimonials,
            'testimonials_count': testimonials_count,
            'projects': projects,
            'prj_img': images,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            quote = form.cleaned_data['quote']
            name = form.cleaned_data['name']
            role = form.cleaned_data['role']
            twitter = form.cleaned_data['twitter']
            website = form.cleaned_data['website']
            try:
                form.save()
                message_out_success = format_html(
                    f'Thanks <strong> {name} </strong>! for leaaving a message. 😊'
                )
                messages.success(
                    request,
                    message_out_success
                )
            except:
                message_out_error = format_html(
                   f'Sorry, <strong> {name} </strong> ! There was a problem submitting your message. 😕'
                )
                messages.error(
                    request,
                    message_out_error
                )
            
            # Redidrect to the same page with message output.
            return redirect('home')
        else:
            form = self.form_class

        context = {
            'form': form
        }
        return render(request, self.template_name, context)

class CaseView(View):
    template_name = 'details.html'
    
    def get(self, request, *args, **kwargs):
        pk = get_object_or_404(Project, id=self.kwargs['pk'])
        project = get_object_or_404(Project, slug=self.kwargs['project'])
        
        query = Project.objects.get(id=pk.id)
        images = ProjectImage.objects.filter(project=project)
        
        print(images, len(images))
        
        context = {
            'pk': pk,
            'project': project,
            'query': query,
            'images': images
        }
        return render(request, self.template_name, context)

class page_not_found_view(TemplateView):
    template_name = '404.html'