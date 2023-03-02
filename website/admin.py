from django.contrib import admin
from .models import AboutInfo, Count, Interest, Testimonial, ProjectCategory, Project, ProjectImage
    
class CountsAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'text', 'updated_at']
    
class InterestAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'color', 'updated_at']
    
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'updated_at']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'updated_at']
    
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'project_date', 'updated_at']
    exclude = ['slug']
    
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'caption', 'updated_at']
    
# admin.site.register(ContactInfo, ContactAdmin)
admin.site.register(AboutInfo)
admin.site.register(Count, CountsAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(ProjectCategory, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)