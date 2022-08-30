from django.contrib import admin


# Register your models here.
from website.models import Project, Resume


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'project_type')
    list_filter = ('project_type',)
    search_fields = ('name',)


class ResumeAdmin(admin.ModelAdmin):
    list_display = ("title", "structure", "resume_type")
    list_filter = ("resume_type",)
    search_fields = ("title", "structure")


admin.site.register(Project, ProjectAdmin)
admin.site.register(Resume, ResumeAdmin)
