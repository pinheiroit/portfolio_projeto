from django.contrib import admin
from .models import Contact, Project , Skill



class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'message', 'created_at')
    search_fields = ['name']
    list_filter = ('created_at')


class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'percentage', 'image')
    search_fields = ('title')
    list_filter = ('percentage')

admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(Skill)

