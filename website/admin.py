from django.contrib import admin

from website.models.biography import Biography


@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    list_display = ("uuid", "created_at", "updated_at")
