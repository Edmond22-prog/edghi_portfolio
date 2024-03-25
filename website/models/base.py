from django.db import models

from website.utils import generate_uuid


class BaseModel(models.Model):
    uuid = models.CharField(
        max_length=100, default=generate_uuid, editable=False, unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
