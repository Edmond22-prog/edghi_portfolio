from django.contrib import admin

from website.models.biography import Biography
from website.models.resume import Resume, ResumeFile


@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    list_display = ("uuid", "created_at", "updated_at")


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("company_name", "title", "employment_type")
    list_filter = ("employment_location", "employment_type")
    


admin.site.register(ResumeFile)
