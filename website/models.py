from django.db import models


class Cv(models.Model):
    file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return str(self.file)

    def get_absolute_url(self):
        return self.file.url
