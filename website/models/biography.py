from django.db import models
from django_quill.fields import QuillField

from website.models.base import BaseModel


class Biography(BaseModel):
    image = models.ImageField(upload_to="profiles/")
    content = QuillField()
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Biographies"

    def __str__(self):
        return self.uuid

    def save(self, *args, **kwargs):
        if not self.created_at:
            filename = f"edmond-makolle-{self.uuid}.png"
            self.image.save(filename, self.image, save=False)

        super().save(*args, **kwargs)
