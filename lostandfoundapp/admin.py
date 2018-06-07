from django.contrib import admin
from .models import LostAndFound

# Register your models here.
"""
Custom LostAndFound model for admin panel.
"""
class LostAndFoundAdmin(admin.ModelAdmin):
    list_display = ['title', 'lost_or_found', 'date_found_or_lost', 'status']
    list_per_page = 10
    fieldsets = [
        ('Lost or Found', {'fields' : ['lost_or_found']}),
        ('Descriptions', {'fields' : ['title', 'description', 'slug', 'image']}),
        ('Contact Informations', {'fields' : ['contact_person_name', 'contact_person_mobile_or_email', ]}),
        ('Other Info', {'fields' : ['date_found_or_lost', 'date_published', 'status', 'date_solved', 'author', 'author_email']}),
    ]
    #date_hierarchy = 'date_found_or_lost'   #archieve or for that specific hierarchy.
    
    class Meta:
        model = LostAndFound

admin.site.site_header = 'LostAndFound Admininstration'
admin.site.register(LostAndFound, LostAndFoundAdmin)