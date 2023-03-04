from django.db import models
from django_quill.fields import QuillField
from colorfield.fields import ColorField
import os
from django.conf import settings
from django.utils.text import slugify

# Create your models here.

class Cv(models.Model):
    file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return str(self.file)

    def get_absolute_url(self):
        return self.file.url


class AboutInfo(models.Model):
    FREELANCE_CHOICES = [
        ('Available | Full time', 'Available | Full time'),
        ('Available | Part time', 'Available | Part time'),
        ('Not Available', 'Not Available'),
    ]
    
    role = models.CharField(max_length=150, default='Python Developer')
    brief = QuillField(default='This is the kind of language I\'m used to speak. Together with some mobile and web dev languages too. 😁😊')
    degree = models.CharField(max_length = 150, default='Master in Computer Science')
    phone = models.CharField(max_length=13, default='+237 6 91 67 83 78')
    email = models.EmailField(default='edghimakoll@gmail.com')
    city = models.CharField(max_length = 150, default='Yaounde, Cameroon')
    freelance = models.CharField(max_length=150, choices=FREELANCE_CHOICES, default='Available | Part time')
    about_text = QuillField(default='Dynamic youth studying Computer Science at the University of Yaounde 1 for the past four years already. I am very passionate about coding and programming and that\'s what I spend most of my time doing')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return 'Last modified on -> ' + str(self.updated_at)
  
    
class Count(models.Model):
    icon = models.CharField(max_length = 150, default='Bootstrap Icon name')
    number = models.PositiveIntegerField()
    text = models.CharField(max_length=150)
    hide = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Count {self.id} : {self.number} - {self.text}'
    
    # Note:
    # The icon library used here is https://icons.getbootstrap.com/.
    # You just need to add the name of the icon i.e.
    # If the icon you want to use is bi-person, you just take 'person' for the icon field.
 
    
class Interest(models.Model):
    icon = models.CharField(max_length = 150, default='Remix Icon name')
    text = models.CharField(max_length = 150)
    color = ColorField(default='#18d26e', format='hexa')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Interest {self.id} : {self.text}'
    
    # Note:
    # The icon library used here is https://remixicon.com/.
    # You just need to add the name of the icon i.e.
    # If the icon you want to use is ri-open-arm-line, you just take 'open-arm-line' for the icon field.
    
    
class Testimonial(models.Model):
    quote = models.TextField(max_length=300)
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    twitter = models.URLField(max_length = 200, null=True, blank=True)
    website = models.URLField(max_length = 200, null=True, blank=True)
    show = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Testimonial {self.id} from {self.name} | {self.role} '
    
    
class ProjectCategory(models.Model):
    CATEGORY_CHOICES = [
        ('Web', 'Web'),
        ('App', 'App'),
        ('Other', 'Other'),
    ]
    
    name = models.CharField(max_length = 150, choices=CATEGORY_CHOICES, default='Other', unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Project Category {self.id} : {self.name}' 
    
    
class Project(models.Model):
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 150, null=True, blank=True)
    client = models.CharField(max_length = 150)
    project_date = models.DateTimeField(auto_now=False)
    project_url = models.URLField(max_length = 200)
    description = QuillField(null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Project {self.id}: {self.name} | {self.client}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)
    
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/')
    caption = models.CharField(max_length = 150)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Project Image {self.id}: {self.caption}'
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = os.path.join('../static/img/realisation.png')
        return url    
