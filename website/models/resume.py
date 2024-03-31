from django.db import models
from django_quill.fields import QuillField

from website.constants import (
    EMPLOYMENT_LOCATIONS,
    EMPLOYMENT_TYPES,
    EmploymentLocation,
    EmploymentType,
)
from website.models.base import BaseModel


class Resume(BaseModel):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = QuillField()
    company_name = models.CharField(max_length=100, blank=False, null=False)
    company_image = models.ImageField(upload_to="companies/", null=True, default=None)
    company_link = models.URLField(blank=True, null=True, default=None)
    company_location = models.CharField(max_length=100, blank=False, null=False)
    employment_type = models.CharField(
        max_length=20, choices=EMPLOYMENT_TYPES, default=EmploymentType.FREELANCE
    )
    employment_location = models.CharField(
        max_length=20,
        choices=EMPLOYMENT_LOCATIONS,
        default=EmploymentLocation.REMOTE,
    )
    start_date = models.CharField(max_length=50, blank=False, null=False)
    end_date = models.CharField(max_length=50, blank=False, null=False)
    
    position = models.IntegerField(unique=True)
    display = models.BooleanField(default=True)
    
    def __str__(self):
        return self.company_name


class ResumeFile(BaseModel):
    file = models.FileField(upload_to="resumes/")
    version = models.IntegerField(unique=True)
    
    def __str__(self):
        return f"Resume-v{self.version}"
    
    def get_absolute_url(self):
        return self.file.url
    
    def save(self, *args, **kwargs):
        if not self.created_at:
            filename = f"edmond-makolle-resume-v{self.version}.pdf"
            self.file.save(filename, self.file, save=False)
        
        super().save(*args, **kwargs)
