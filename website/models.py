from django.db import models

PROJECT_TYPES = [
    ("App", "Application"),
    ("Scripts", "Scripts"),
    ("Web", "Website"),
]

RESUME_TYPES = [
    ("Community", "Community"),
    ("Professional", "Professional"),
]


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    url = models.CharField(max_length=255, blank=False, null=False)
    project_type = models.CharField(choices=PROJECT_TYPES, max_length=50)

    def __str__(self):
        return self.name


class Resume(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    start = models.CharField(max_length=50, blank=False, null=False)
    end = models.CharField(max_length=50, blank=False, null=False)
    structure = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    resume_type = models.CharField(choices=RESUME_TYPES, max_length=50)

    def __str__(self):
        return self.title
